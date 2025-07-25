# YOLOR PyTorch utils

import datetime
import logging
import math
import os
import platform
import subprocess
import time
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path

import numpy as np
import torch
import torch.backends.cudnn as cudnn
import torch.nn as nn
import torch.nn.functional as F
import torchvision

try:
    import thop  # for FLOPS computation
except ImportError:
    thop = None
logger = logging.getLogger(__name__)

try:
    from pytorch_nndct.apis import torch_quantizer
    from pytorch_nndct.nn import QuantStub, DeQuantStub
    from pytorch_nndct import QatProcessor
    NNDCT_AVAILABLE = True
except ImportError:
    NNDCT_AVAILABLE = False


@contextmanager
def torch_distributed_zero_first(local_rank: int):
    """
    Decorator to make all processes in distributed training wait for each local_master to do something.
    """
    if local_rank not in [-1, 0]:
        torch.distributed.barrier()
    yield
    if local_rank == 0:
        torch.distributed.barrier()


def init_torch_seeds(seed=0):
    # Speed-reproducibility tradeoff https://pytorch.org/docs/stable/notes/randomness.html
    torch.manual_seed(seed)
    if seed == 0:  # slower, more reproducible
        cudnn.benchmark, cudnn.deterministic = False, True
    else:  # faster, less reproducible
        cudnn.benchmark, cudnn.deterministic = True, False


def date_modified(path=__file__):
    # return human-readable file modification date, i.e. '2021-3-26'
    t = datetime.datetime.fromtimestamp(Path(path).stat().st_mtime)
    return f'{t.year}-{t.month}-{t.day}'


def git_describe(path=Path(__file__).parent):  # path must be a directory
    # return human-readable git description, i.e. v5.0-5-g3e25f1e https://git-scm.com/docs/git-describe
    s = f'git -C {path} describe --tags --long --always'
    try:
        return subprocess.check_output(s, shell=True, stderr=subprocess.STDOUT).decode()[:-1]
    except subprocess.CalledProcessError as e:
        return ''  # not a git repository


def select_device(device='', batch_size=None):
    # device = 'cpu' or '0' or '0,1,2,3'
    s = f'YOLOR 🚀 {git_describe() or date_modified()} torch {torch.__version__} '  # string
    cpu = device.lower() == 'cpu'
    if cpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # force torch.cuda.is_available() = False
    elif device:  # non-cpu device requested
        os.environ['CUDA_VISIBLE_DEVICES'] = device  # set environment variable
        assert torch.cuda.is_available(), f'CUDA unavailable, invalid device {device} requested'  # check availability

    cuda = not cpu and torch.cuda.is_available()
    if cuda:
        n = torch.cuda.device_count()
        if n > 1 and batch_size:  # check that batch_size is compatible with device_count
            assert batch_size % n == 0, f'batch-size {batch_size} not multiple of GPU count {n}'
        space = ' ' * len(s)
        for i, d in enumerate(device.split(',') if device else range(n)):
            p = torch.cuda.get_device_properties(i)
            s += f"{'' if i == 0 else space}CUDA:{d} ({p.name}, {p.total_memory / 1024 ** 2}MB)\n"  # bytes to MB
    else:
        s += 'CPU\n'

    logger.info(s.encode().decode('ascii', 'ignore') if platform.system() == 'Windows' else s)  # emoji-safe
    return torch.device('cuda:0' if cuda else 'cpu')


def time_synchronized():
    # pytorch-accurate time
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return time.time()


def profile(x, ops, n=100, device=None):
    # profile a pytorch module or list of modules. Example usage:
    #     x = torch.randn(16, 3, 640, 640)  # input
    #     m1 = lambda x: x * torch.sigmoid(x)
    #     m2 = nn.SiLU()
    #     profile(x, [m1, m2], n=100)  # profile speed over 100 iterations

    device = device or torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    x = x.to(device)
    x.requires_grad = True
    print(torch.__version__, device.type, torch.cuda.get_device_properties(0) if device.type == 'cuda' else '')
    print(f"\n{'Params':>12s}{'GFLOPS':>12s}{'forward (ms)':>16s}{'backward (ms)':>16s}{'input':>24s}{'output':>24s}")
    for m in ops if isinstance(ops, list) else [ops]:
        m = m.to(device) if hasattr(m, 'to') else m  # device
        m = m.half() if hasattr(m, 'half') and isinstance(x, torch.Tensor) and x.dtype is torch.float16 else m  # type
        dtf, dtb, t = 0., 0., [0., 0., 0.]  # dt forward, backward
        try:
            flops = thop.profile(m, inputs=(x,), verbose=False)[0] / 1E9 * 2  # GFLOPS
        except:
            flops = 0

        for _ in range(n):
            t[0] = time_synchronized()
            y = m(x)
            t[1] = time_synchronized()
            try:
                _ = y.sum().backward()
                t[2] = time_synchronized()
            except:  # no backward method
                t[2] = float('nan')
            dtf += (t[1] - t[0]) * 1000 / n  # ms per op forward
            dtb += (t[2] - t[1]) * 1000 / n  # ms per op backward

        s_in = tuple(x.shape) if isinstance(x, torch.Tensor) else 'list'
        s_out = tuple(y.shape) if isinstance(y, torch.Tensor) else 'list'
        p = sum(list(x.numel() for x in m.parameters())) if isinstance(m, nn.Module) else 0  # parameters
        print(f'{p:12}{flops:12.4g}{dtf:16.4g}{dtb:16.4g}{str(s_in):>24s}{str(s_out):>24s}')


def is_parallel(model):
    return type(model) in (nn.parallel.DataParallel, nn.parallel.DistributedDataParallel)


def intersect_dicts(da, db, exclude=()):
    # Dictionary intersection of matching keys and shapes, omitting 'exclude' keys, using da values
    return {k: v for k, v in da.items() if k in db and not any(x in k for x in exclude) and v.shape == db[k].shape}


def initialize_weights(model):
    for m in model.modules():
        t = type(m)
        if t is nn.Conv2d:
            pass  # nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        elif t is nn.BatchNorm2d:
            m.eps = 1e-3
            m.momentum = 0.03
        elif t in [nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6]:
            m.inplace = True


def find_modules(model, mclass=nn.Conv2d):
    # Finds layer indices matching module class 'mclass'
    return [i for i, m in enumerate(model.module_list) if isinstance(m, mclass)]


def sparsity(model):
    # Return global model sparsity
    a, b = 0., 0.
    for p in model.parameters():
        a += p.numel()
        b += (p == 0).sum()
    return b / a


def prune(model, amount=0.3):
    # Prune model to requested global sparsity
    import torch.nn.utils.prune as prune
    print('Pruning model... ', end='')
    for name, m in model.named_modules():
        if isinstance(m, nn.Conv2d):
            prune.l1_unstructured(m, name='weight', amount=amount)  # prune
            prune.remove(m, 'weight')  # make permanent
    print(' %.3g global sparsity' % sparsity(model))


def fuse_conv_and_bn(conv, bn):
    # Fuse convolution and batchnorm layers https://tehnokv.com/posts/fusing-batchnorm-and-conv/
    fusedconv = nn.Conv2d(conv.in_channels,
                          conv.out_channels,
                          kernel_size=conv.kernel_size,
                          stride=conv.stride,
                          padding=conv.padding,
                          groups=conv.groups,
                          bias=True).requires_grad_(False).to(conv.weight.device)

    # prepare filters
    w_conv = conv.weight.clone().view(conv.out_channels, -1)
    w_bn = torch.diag(bn.weight.div(torch.sqrt(bn.eps + bn.running_var)))
    fusedconv.weight.copy_(torch.mm(w_bn, w_conv).view(fusedconv.weight.shape))

    # prepare spatial bias
    b_conv = torch.zeros(conv.weight.size(0), device=conv.weight.device) if conv.bias is None else conv.bias
    b_bn = bn.bias - bn.weight.mul(bn.running_mean).div(torch.sqrt(bn.running_var + bn.eps))
    fusedconv.bias.copy_(torch.mm(w_bn, b_conv.reshape(-1, 1)).reshape(-1) + b_bn)

    return fusedconv


def model_info(model, verbose=False, img_size=640):
    # Model information. img_size may be int or list, i.e. img_size=640 or img_size=[640, 320]
    n_p = sum(x.numel() for x in model.parameters())  # number parameters
    n_g = sum(x.numel() for x in model.parameters() if x.requires_grad)  # number gradients
    if verbose:
        print('%5s %40s %9s %12s %20s %10s %10s' % ('layer', 'name', 'gradient', 'parameters', 'shape', 'mu', 'sigma'))
        for i, (name, p) in enumerate(model.named_parameters()):
            name = name.replace('module_list.', '')
            print('%5g %40s %9s %12g %20s %10.3g %10.3g' %
                  (i, name, p.requires_grad, p.numel(), list(p.shape), p.mean(), p.std()))

    try:  # FLOPS
        from thop import profile
        stride = max(int(model.stride.max()), 32) if hasattr(model, 'stride') else 32
        img = torch.zeros((1, model.yaml.get('ch', 3), stride, stride), device=next(model.parameters()).device)  # input
        flops = profile(deepcopy(model), inputs=(img,), verbose=False)[0] / 1E9 * 2  # stride GFLOPS
        img_size = img_size if isinstance(img_size, list) else [img_size, img_size]  # expand if int/float
        fs = ', %.1f GFLOPS' % (flops * img_size[0] / stride * img_size[1] / stride)  # 640x640 GFLOPS
    except (ImportError, Exception):
        fs = ''

    logger.info(f"Model Summary: {len(list(model.modules()))} layers, {n_p} parameters, {n_g} gradients{fs}")


def load_classifier(name='resnet101', n=2):
    # Loads a pretrained model reshaped to n-class output
    model = torchvision.models.__dict__[name](pretrained=True)

    # ResNet model properties
    # input_size = [3, 224, 224]
    # input_space = 'RGB'
    # input_range = [0, 1]
    # mean = [0.485, 0.456, 0.406]
    # std = [0.229, 0.224, 0.225]

    # Reshape output to n classes
    filters = model.fc.weight.shape[1]
    model.fc.bias = nn.Parameter(torch.zeros(n), requires_grad=True)
    model.fc.weight = nn.Parameter(torch.zeros(n, filters), requires_grad=True)
    model.fc.out_features = n
    return model


def scale_img(img, ratio=1.0, same_shape=False, gs=32):  # img(16,3,256,416)
    # scales img(bs,3,y,x) by ratio constrained to gs-multiple
    if ratio == 1.0:
        return img
    else:
        h, w = img.shape[2:]
        s = (int(h * ratio), int(w * ratio))  # new size
        img = F.interpolate(img, size=s, mode='bilinear', align_corners=False)  # resize
        if not same_shape:  # pad/crop img
            h, w = [math.ceil(x * ratio / gs) * gs for x in (h, w)]
        return F.pad(img, [0, w - s[1], 0, h - s[0]], value=0.447)  # value = imagenet mean


def copy_attr(a, b, include=(), exclude=()):
    # Copy attributes from b to a, options to only include [...] and to exclude [...]
    for k, v in b.__dict__.items():
        if (len(include) and k not in include) or k.startswith('_') or k in exclude:
            continue
        else:
            setattr(a, k, v)


class ModelEMA:
    """ Model Exponential Moving Average from https://github.com/rwightman/pytorch-image-models
    Keep a moving average of everything in the model state_dict (parameters and buffers).
    This is intended to allow functionality like
    https://www.tensorflow.org/api_docs/python/tf/train/ExponentialMovingAverage
    A smoothed version of the weights is necessary for some training schemes to perform well.
    This class is sensitive where it is initialized in the sequence of model init,
    GPU assignment and distributed training wrappers.
    """

    def __init__(self, model, decay=0.9999, updates=0):
        # Create EMA
        self.ema = deepcopy(model.module if is_parallel(model) else model).eval()  # FP32 EMA
        # if next(model.parameters()).device.type != 'cpu':
        #     self.ema.half()  # FP16 EMA
        self.updates = updates  # number of EMA updates
        self.decay = lambda x: decay * (1 - math.exp(-x / 2000))  # decay exponential ramp (to help early epochs)
        for p in self.ema.parameters():
            p.requires_grad_(False)

    def update(self, model):
        # Update EMA parameters
        with torch.no_grad():
            self.updates += 1
            d = self.decay(self.updates)

            msd = model.module.state_dict() if is_parallel(model) else model.state_dict()  # model state_dict
            for k, v in self.ema.state_dict().items():
                if v.dtype.is_floating_point:
                    v *= d
                    v += (1. - d) * msd[k].detach()

    def update_attr(self, model, include=(), exclude=('process_group', 'reducer')):
        # Update EMA attributes
        copy_attr(self.ema, model, include, exclude)


class BatchNormXd(torch.nn.modules.batchnorm._BatchNorm):
    def _check_input_dim(self, input):
        # The only difference between BatchNorm1d, BatchNorm2d, BatchNorm3d, etc
        # is this method that is overwritten by the sub-class
        # This original goal of this method was for tensor sanity checks
        # If you're ok bypassing those sanity checks (eg. if you trust your inference
        # to provide the right dimensional inputs), then you can just use this method
        # for easy conversion from SyncBatchNorm
        # (unfortunately, SyncBatchNorm does not store the original class - if it did
        #  we could return the one that was originally created)
        return

def revert_sync_batchnorm(module):
    # this is very similar to the function that it is trying to revert:
    # https://github.com/pytorch/pytorch/blob/c8b3686a3e4ba63dc59e5dcfe5db3430df256833/torch/nn/modules/batchnorm.py#L679
    module_output = module
    if isinstance(module, torch.nn.modules.batchnorm.SyncBatchNorm):
        new_cls = BatchNormXd
        module_output = BatchNormXd(module.num_features,
                                               module.eps, module.momentum,
                                               module.affine,
                                               module.track_running_stats)
        if module.affine:
            with torch.no_grad():
                module_output.weight = module.weight
                module_output.bias = module.bias
        module_output.running_mean = module.running_mean
        module_output.running_var = module.running_var
        module_output.num_batches_tracked = module.num_batches_tracked
        if hasattr(module, "qconfig"):
            module_output.qconfig = module.qconfig
    for name, child in module.named_children():
        module_output.add_module(name, revert_sync_batchnorm(child))
    del module
    return module_output


class TracedModel(nn.Module):

    def __init__(self, model=None, device=None, img_size=(640,640)): 
        super(TracedModel, self).__init__()
        
        print(" Convert model to Traced-model... ") 
        self.stride = model.stride
        self.names = model.names
        self.model = model

        self.model = revert_sync_batchnorm(self.model)
        self.model.to('cpu')
        self.model.eval()

        self.detect_layer = self.model.model[-1]
        self.model.traced = True
        
        rand_example = torch.rand(1, 3, img_size, img_size)
        # dry run
        self.model(rand_example)
        
        traced_script_module = torch.jit.trace(self.model, rand_example, strict=False)
        #traced_script_module = torch.jit.script(self.model)
        traced_script_module.save("traced_model.pt")
        print(" traced_script_module saved! ")
        self.model = traced_script_module
        self.model.to(device)
        self.detect_layer.to(device)
        print(" model is traced! \n") 

    def forward(self, x, augment=False, profile=False):
        out = self.model(x)
        out = self.detect_layer(out)
        return out

class ONNXModel(nn.Module):

    def __init__(self, model, onnx_file, device=None, img_size=640, runtime='onnx', data_type='fp32'): 
        super(ONNXModel, self).__init__()
        
        print(" Convert model to Traced-model... ") 
        self.stride = model.stride
        self.names = model.names
        self.device = device
        self.runtime = runtime
        self.data_type = data_type

        if self.runtime == 'onnx':
            import onnxruntime
            self.session = onnxruntime.InferenceSession(onnx_file, None)
        elif self.runtime == 'torchscript':
            from utils.general import non_max_suppression
            self.script_model = torch.jit.load(onnx_file, map_location=device).eval()
            self.non_max_suppression = lambda x: non_max_suppression(x, 0.001, 0.65, classes=None, agnostic=False)
            # nndct model
            if self.data_type == 'int8':
                from models.yolo import Detect, IDetect, IAuxDetect, IKeypoint, IBin
                self.detect_layer = deepcopy(model.model[-1])
                if isinstance(self.detect_layer, (Detect, IDetect)):
                    self.detect_layer.m = nn.ModuleList(nn.Identity() for _ in self.detect_layer.m)
                elif isinstance(self.detect_layer, (IAuxDetect, IKeypoint, IBin)):
                    raise NotImplementedError
                self.detect_layer.to(device)
        elif self.runtime == 'migraphx':
            import migraphx
            self.session = migraphx.parse_onnx(onnx_file)
            self.session.compile(migraphx.get_target("gpu"))
        else:
            raise ValueError(f"Invalid ONNX runtime: {self.runtime}")

    def forward(self, x, augment=False, profile=False):
        if self.runtime == 'onnx':
            pred = torch.tensor(self.session.run([self.session.get_outputs()[0].name], {self.session.get_inputs()[0].name: x.cpu().numpy()})).to(self.device)
            if len(pred[0]) == 0:
                return []
            pred = pred[0]
            box = pred[:, 1:5]
            cls = pred[:, 5:6]
            score = pred[:, 6:7]
            pred = [torch.cat([box, score, cls], -1)]
        elif self.runtime == 'torchscript':
            if self.data_type == 'int8':
                pred = list(self.script_model(x))
                pred = self.detect_layer(pred)[0]
                pred = self.non_max_suppression(pred)[0]
            else:
                pred = self.script_model(x)[0]
                pred = self.non_max_suppression(pred)[0]
            box = pred[:, 0:4]
            cls = pred[:, 5:6]
            score = pred[:, 4:5]
            pred = [torch.cat([box, score, cls], -1)]
        elif self.runtime == 'migraphx':
            if self.data_type=='fp16':
                x = x.half()
            pred = self.session.run({'images': x.cpu().numpy()})[0]
            pred = torch.tensor(np.array(pred)).to(self.device)
            box = pred[:, 1:5]
            cls = pred[:, 5:6]
            score = pred[:, 6:7]
            pred = [torch.cat([box, score, cls], -1)]
        return pred


class NNDctDetect(nn.Module):

    def __init__(self, m, nl):
        super(NNDctDetect, self).__init__()
        if not NNDCT_AVAILABLE:
            raise ModuleNotFoundError("pytorch_nndct is not installed. Please install it to use NNDctDetect.")
        self.m = m
        self.nl = nl
        dequant = []
        for i in range(self.nl):
            dequant.append(DeQuantStub())
        self.dequant = nn.ModuleList(dequant)
            
    
    def forward(self, x):
        for i in range(self.nl):
            x[i] = self.dequant[i](self.m[i](x[i]))  # conv
        return x
    
class NNDctModel(nn.Module):

    def __init__(self, model=None, device=None, img_size=(640,640), nndct_bitwidth=8, output_dir='nndct'):
        super(NNDctModel, self).__init__()
        if not NNDCT_AVAILABLE:
            raise ModuleNotFoundError("pytorch_nndct is not installed. Please install it to use NNDctModel.")
        model = deepcopy(model)
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('--quant_mode', default='calib', choices=['float', 'calib', 'test'], help='quant mode')
        parser.add_argument('--dump_model', action='store_true', help='dump model')
        opt, _ = parser.parse_known_args()
        self.quant_mode = opt.quant_mode
        self.dump_model = opt.dump_model
        if self.dump_model:
            if self.quant_mode != 'test':
                raise ValueError
        from models.yolo import Detect, IDetect, IAuxDetect, IKeypoint, IBin
        
        print(" Convert model to Traced-model... ")
        self.stride = model.stride
        self.names = model.names
        self.model = model

        self.model = revert_sync_batchnorm(self.model)
        # fuse multi time will cause invalid param value
        # with torch.no_grad():
        #     self.model = model.fuse() # make sure the model is fused
        quant = QuantStub()
        setattr(self.model, 'quant', quant)
        with torch.no_grad():
            for k, v in self.model.named_parameters():
                v.requires_grad = True  # train all layers
                if 'implicit' in k:
                    print('freezing %s' % k)
                    v.requires_grad = False
        self.model.to('cpu')
        self.model.eval()

        self.detect_layer = self.model.model[-1]
        if isinstance(self.detect_layer, (Detect, IDetect)):
            modules = list(self.model.model)
            m_ = NNDctDetect(self.detect_layer.m, self.detect_layer.nl)
            m_.type = 'NNDctDetect'
            m_.i = modules[-1].i
            modules[-1].i += 1
            m_.f = modules[-1].f
            m_.np = sum([x.numel() for x in m_.parameters()])  # number params
            modules.insert(-1, m_)
            self.detect_layer.m = nn.ModuleList(nn.Identity() for _ in self.detect_layer.m)
            modules[-1].f = -1 # from previous
            modules[-1].np = sum([x.numel() for x in modules[-1].parameters()])
            self.model.model = nn.Sequential(*modules)
        elif isinstance(self.detect_layer, (IAuxDetect, IKeypoint, IBin)):
            raise NotImplementedError
        self.model.traced = True
        self.output_dir = output_dir
        
        rand_example = torch.rand(1, 3, img_size, img_size)
        # Dry run
        model(rand_example)
        
        if self.quant_mode == 'float':
            # traced_script_module = torch.jit.trace(self.model, rand_example, strict=False)
            #traced_script_module = torch.jit.script(self.model)
            # traced_script_module.save("traced_model.pt")
            # print(" traced_script_module saved! ")
            self.quantizer = None
            self.model = model
        else:
            quantizer = torch_quantizer(quant_mode=self.quant_mode,
                                        bitwidth=nndct_bitwidth,
                                        module=model,
                                        input_args=rand_example,
                                        output_dir=output_dir)
            quant_model = quantizer.quant_model
            self.quantizer = quantizer
            self.model = quant_model
        self.model.to(device)
        self.detect_layer.to(device)
        print(" model is traced! \n") 

    def forward(self, x, augment=False, profile=False):
        out = self.model(x)
        out = list(out)
        out = self.detect_layer(out)
        return out

    def export(self):
        if self.quant_mode == 'calib':
            self.quantizer.export_quant_config()
        elif self.quant_mode == 'test':
            self.quantizer.export_onnx_model(output_dir=self.output_dir, verbose=False, dynamic_batch=True, opset_version=12)
            self.quantizer.export_torch_script(output_dir=self.output_dir, verbose=False)
            self.quantizer.export_xmodel(output_dir=self.output_dir, deploy_check=True, dynamic_batch=True)

def get_qat_model(model, device=None, img_size=640, nndct_bitwidth=8, output_dir='nndct'):
    if not NNDCT_AVAILABLE:
        raise ModuleNotFoundError("pytorch_nndct is not installed. Please install it to use get_qat_model.")
    from models.yolo import Detect, IDetect, IAuxDetect, IKeypoint, IBin
    model = deepcopy(model)
    quant = QuantStub()
    model.train()  
    setattr(model, 'quant', quant)
    for k, v in model.named_parameters():
        v.requires_grad = True  # train all layers
        if 'implicit' in k:
            print('freezing %s' % k)
            v.requires_grad = False

    detect_layer = model.model[-1]
    if isinstance(detect_layer, (Detect, IDetect)):
        modules = list(model.model)
        m_ = NNDctDetect(detect_layer.m, detect_layer.nl)
        m_.type = 'NNDctDetect'
        m_.i = modules[-1].i
        modules[-1].i += 1
        m_.f = modules[-1].f
        m_.np = sum([x.numel() for x in m_.parameters()])  # number params
        modules.insert(-1, m_)
        detect_layer.m = nn.ModuleList(nn.Identity() for _ in detect_layer.m)
        modules[-1].f = -1 # from previous
        modules[-1].np = sum([x.numel() for x in modules[-1].parameters()])
        model.model = nn.Sequential(*modules)
    elif isinstance(detect_layer, (IAuxDetect, IKeypoint, IBin)):
        raise NotImplementedError
    model.traced = True   
    model.to(device)
    # Image sizes
    rand_example = torch.rand(1, 3, img_size, img_size).to(next(model.parameters()).device)
    # Dry run
    model(rand_example)
    qat_processor = QatProcessor(model, (rand_example,), bitwidth=nndct_bitwidth, mix_bit=False)
    qat_model = qat_processor.trainable_model()
    qat_model.stride = model.stride
    qat_model.names = model.names
    qat_model.origin_forward = qat_model.forward
    def forward(instance, x):
        x = instance.origin_forward(x)
        x = detect_layer(x)
        return x
    from types import MethodType
    qat_model.new_forward = MethodType(forward, qat_model)
    qat_model.forward = qat_model.new_forward
    return qat_model, qat_processor
