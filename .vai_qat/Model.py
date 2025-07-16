# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class Model(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(Model, self).__init__()
        self.module_0 = py_nndct.nn.Input() #Model::input_0
        self.module_1 = py_nndct.nn.quant_input() #Model::Model/QuantStub[quant]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[0]/Conv2d[conv]/input.3
        self.module_3 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[0]/Hardswish[act]/input.7
        self.module_4 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[1]/Conv2d[conv]/input.9
        self.module_5 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[1]/Hardswish[act]/input.13
        self.module_6 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[2]/Conv2d[conv]/input.15
        self.module_7 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[2]/Hardswish[act]/input.19
        self.module_8 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[3]/Conv2d[conv]/input.21
        self.module_9 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[3]/Hardswish[act]/input.25
        self.module_10 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[4]/Conv2d[conv]/input.27
        self.module_11 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[4]/Hardswish[act]/9952
        self.module_12 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[5]/Conv2d[conv]/input.31
        self.module_13 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[5]/Hardswish[act]/input.35
        self.module_14 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[6]/Conv2d[conv]/input.37
        self.module_15 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[6]/Hardswish[act]/input.41
        self.module_16 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[7]/Conv2d[conv]/input.43
        self.module_17 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[7]/Hardswish[act]/input.47
        self.module_18 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[8]/Conv2d[conv]/input.49
        self.module_19 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[8]/Hardswish[act]/input.53
        self.module_20 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[9]/Conv2d[conv]/input.55
        self.module_21 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[9]/Hardswish[act]/10082
        self.module_22 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[10]/Cat[cat]/input.59
        self.module_23 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[11]/Conv2d[conv]/input.61
        self.module_24 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[11]/Hardswish[act]/input.71
        self.module_25 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #Model::Model/MP[model]/MP[12]/MaxPool2d[m]/input.65
        self.module_26 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[13]/Conv2d[conv]/input.67
        self.module_27 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[13]/Hardswish[act]/10151
        self.module_28 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[14]/Conv2d[conv]/input.73
        self.module_29 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[14]/Hardswish[act]/input.77
        self.module_30 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[15]/Conv2d[conv]/input.79
        self.module_31 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[15]/Hardswish[act]/10203
        self.module_32 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[16]/Cat[cat]/input.83
        self.module_33 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[17]/Conv2d[conv]/input.85
        self.module_34 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[17]/Hardswish[act]/10232
        self.module_35 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[18]/Conv2d[conv]/input.89
        self.module_36 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[18]/Hardswish[act]/input.93
        self.module_37 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[19]/Conv2d[conv]/input.95
        self.module_38 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[19]/Hardswish[act]/input.99
        self.module_39 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[20]/Conv2d[conv]/input.101
        self.module_40 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[20]/Hardswish[act]/input.105
        self.module_41 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[21]/Conv2d[conv]/input.107
        self.module_42 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[21]/Hardswish[act]/input.111
        self.module_43 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[22]/Conv2d[conv]/input.113
        self.module_44 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[22]/Hardswish[act]/10362
        self.module_45 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[23]/Cat[cat]/input.117
        self.module_46 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[24]/Conv2d[conv]/input.119
        self.module_47 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[24]/Hardswish[act]/input.129
        self.module_48 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #Model::Model/MP[model]/MP[25]/MaxPool2d[m]/input.123
        self.module_49 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[26]/Conv2d[conv]/input.125
        self.module_50 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[26]/Hardswish[act]/10431
        self.module_51 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[27]/Conv2d[conv]/input.131
        self.module_52 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[27]/Hardswish[act]/input.135
        self.module_53 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[28]/Conv2d[conv]/input.137
        self.module_54 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[28]/Hardswish[act]/10483
        self.module_55 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[29]/Cat[cat]/input.141
        self.module_56 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[30]/Conv2d[conv]/input.143
        self.module_57 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[30]/Hardswish[act]/10512
        self.module_58 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[31]/Conv2d[conv]/input.147
        self.module_59 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[31]/Hardswish[act]/input.151
        self.module_60 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[32]/Conv2d[conv]/input.153
        self.module_61 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[32]/Hardswish[act]/input.157
        self.module_62 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[33]/Conv2d[conv]/input.159
        self.module_63 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[33]/Hardswish[act]/input.163
        self.module_64 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[34]/Conv2d[conv]/input.165
        self.module_65 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[34]/Hardswish[act]/input.169
        self.module_66 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[35]/Conv2d[conv]/input.171
        self.module_67 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[35]/Hardswish[act]/10642
        self.module_68 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[36]/Cat[cat]/input.175
        self.module_69 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=1024, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[37]/Conv2d[conv]/input.177
        self.module_70 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[37]/Hardswish[act]/input.187
        self.module_71 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #Model::Model/MP[model]/MP[38]/MaxPool2d[m]/input.181
        self.module_72 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[39]/Conv2d[conv]/input.183
        self.module_73 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[39]/Hardswish[act]/10711
        self.module_74 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[40]/Conv2d[conv]/input.189
        self.module_75 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[40]/Hardswish[act]/input.193
        self.module_76 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[41]/Conv2d[conv]/input.195
        self.module_77 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[41]/Hardswish[act]/10763
        self.module_78 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[42]/Cat[cat]/input.199
        self.module_79 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[43]/Conv2d[conv]/input.201
        self.module_80 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[43]/Hardswish[act]/10792
        self.module_81 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[44]/Conv2d[conv]/input.205
        self.module_82 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[44]/Hardswish[act]/input.209
        self.module_83 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[45]/Conv2d[conv]/input.211
        self.module_84 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[45]/Hardswish[act]/input.215
        self.module_85 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[46]/Conv2d[conv]/input.217
        self.module_86 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[46]/Hardswish[act]/input.221
        self.module_87 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[47]/Conv2d[conv]/input.223
        self.module_88 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[47]/Hardswish[act]/input.227
        self.module_89 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[48]/Conv2d[conv]/input.229
        self.module_90 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[48]/Hardswish[act]/10922
        self.module_91 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[49]/Cat[cat]/input.233
        self.module_92 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=1024, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[50]/Conv2d[conv]/input.235
        self.module_93 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[50]/Hardswish[act]/input.239
        self.module_94 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv1]/Conv2d[conv]/input.241
        self.module_95 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv1]/Hardswish[act]/input.245
        self.module_96 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv3]/Conv2d[conv]/input.247
        self.module_97 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv3]/Hardswish[act]/input.251
        self.module_98 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv4]/Conv2d[conv]/input.253
        self.module_99 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv4]/Hardswish[act]/11029
        self.module_100 = py_nndct.nn.MaxPool2d(kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], ceil_mode=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/MaxPool2d[m]/ModuleList[0]/11043
        self.module_101 = py_nndct.nn.MaxPool2d(kernel_size=[9, 9], stride=[1, 1], padding=[4, 4], dilation=[1, 1], ceil_mode=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/MaxPool2d[m]/ModuleList[1]/11057
        self.module_102 = py_nndct.nn.MaxPool2d(kernel_size=[13, 13], stride=[1, 1], padding=[6, 6], dilation=[1, 1], ceil_mode=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/MaxPool2d[m]/ModuleList[2]/11071
        self.module_103 = py_nndct.nn.Cat() #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Cat[cat]/input.257
        self.module_104 = py_nndct.nn.Conv2d(in_channels=2048, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv5]/Conv2d[conv]/input.259
        self.module_105 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv5]/Hardswish[act]/input.263
        self.module_106 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv6]/Conv2d[conv]/input.265
        self.module_107 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv6]/Hardswish[act]/11126
        self.module_108 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv2]/Conv2d[conv]/input.269
        self.module_109 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv2]/Hardswish[act]/11152
        self.module_110 = py_nndct.nn.Cat() #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Cat[cat2]/input.273
        self.module_111 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv7]/Conv2d[conv]/input.275
        self.module_112 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/SPPCSPC[model]/SPPCSPC[51]/Conv[cv7]/Hardswish[act]/input.279
        self.module_113 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[52]/Conv2d[conv]/input.281
        self.module_114 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[52]/Hardswish[act]/input.285
        self.module_115 = py_nndct.nn.Interpolate() #Model::Model/Upsample[model]/Upsample[53]/11212
        self.module_116 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[54]/Conv2d[conv]/input.287
        self.module_117 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[54]/Hardswish[act]/11238
        self.module_118 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[55]/Cat[cat]/input.291
        self.module_119 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[56]/Conv2d[conv]/input.293
        self.module_120 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[56]/Hardswish[act]/11267
        self.module_121 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[57]/Conv2d[conv]/input.297
        self.module_122 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[57]/Hardswish[act]/input.301
        self.module_123 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[58]/Conv2d[conv]/input.303
        self.module_124 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[58]/Hardswish[act]/input.307
        self.module_125 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[59]/Conv2d[conv]/input.309
        self.module_126 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[59]/Hardswish[act]/input.313
        self.module_127 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[60]/Conv2d[conv]/input.315
        self.module_128 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[60]/Hardswish[act]/input.319
        self.module_129 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[61]/Conv2d[conv]/input.321
        self.module_130 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[61]/Hardswish[act]/11397
        self.module_131 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[62]/Cat[cat]/input.325
        self.module_132 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[63]/Conv2d[conv]/input.327
        self.module_133 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[63]/Hardswish[act]/input.331
        self.module_134 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[64]/Conv2d[conv]/input.333
        self.module_135 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[64]/Hardswish[act]/input.337
        self.module_136 = py_nndct.nn.Interpolate() #Model::Model/Upsample[model]/Upsample[65]/11457
        self.module_137 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[66]/Conv2d[conv]/input.339
        self.module_138 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[66]/Hardswish[act]/11483
        self.module_139 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[67]/Cat[cat]/input.343
        self.module_140 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[68]/Conv2d[conv]/input.345
        self.module_141 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[68]/Hardswish[act]/11512
        self.module_142 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[69]/Conv2d[conv]/input.349
        self.module_143 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[69]/Hardswish[act]/input.353
        self.module_144 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[70]/Conv2d[conv]/input.355
        self.module_145 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[70]/Hardswish[act]/input.359
        self.module_146 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[71]/Conv2d[conv]/input.361
        self.module_147 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[71]/Hardswish[act]/input.365
        self.module_148 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[72]/Conv2d[conv]/input.367
        self.module_149 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[72]/Hardswish[act]/input.371
        self.module_150 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[73]/Conv2d[conv]/input.373
        self.module_151 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[73]/Hardswish[act]/11642
        self.module_152 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[74]/Cat[cat]/input.377
        self.module_153 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[75]/Conv2d[conv]/input.379
        self.module_154 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[75]/Hardswish[act]/input.389
        self.module_155 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #Model::Model/MP[model]/MP[76]/MaxPool2d[m]/input.383
        self.module_156 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[77]/Conv2d[conv]/input.385
        self.module_157 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[77]/Hardswish[act]/11711
        self.module_158 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[78]/Conv2d[conv]/input.391
        self.module_159 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[78]/Hardswish[act]/input.395
        self.module_160 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[79]/Conv2d[conv]/input.397
        self.module_161 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[79]/Hardswish[act]/11763
        self.module_162 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[80]/Cat[cat]/input.401
        self.module_163 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[81]/Conv2d[conv]/input.403
        self.module_164 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[81]/Hardswish[act]/11792
        self.module_165 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[82]/Conv2d[conv]/input.407
        self.module_166 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[82]/Hardswish[act]/input.411
        self.module_167 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[83]/Conv2d[conv]/input.413
        self.module_168 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[83]/Hardswish[act]/input.417
        self.module_169 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[84]/Conv2d[conv]/input.419
        self.module_170 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[84]/Hardswish[act]/input.423
        self.module_171 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[85]/Conv2d[conv]/input.425
        self.module_172 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[85]/Hardswish[act]/input.429
        self.module_173 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[86]/Conv2d[conv]/input.431
        self.module_174 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[86]/Hardswish[act]/11922
        self.module_175 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[87]/Cat[cat]/input.435
        self.module_176 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[88]/Conv2d[conv]/input.437
        self.module_177 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[88]/Hardswish[act]/input.447
        self.module_178 = py_nndct.nn.MaxPool2d(kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #Model::Model/MP[model]/MP[89]/MaxPool2d[m]/input.441
        self.module_179 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[90]/Conv2d[conv]/input.443
        self.module_180 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[90]/Hardswish[act]/11991
        self.module_181 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[91]/Conv2d[conv]/input.449
        self.module_182 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[91]/Hardswish[act]/input.453
        self.module_183 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[92]/Conv2d[conv]/input.455
        self.module_184 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[92]/Hardswish[act]/12043
        self.module_185 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[93]/Cat[cat]/input.459
        self.module_186 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[94]/Conv2d[conv]/input.461
        self.module_187 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[94]/Hardswish[act]/12072
        self.module_188 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[95]/Conv2d[conv]/input.465
        self.module_189 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[95]/Hardswish[act]/input.469
        self.module_190 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[96]/Conv2d[conv]/input.471
        self.module_191 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[96]/Hardswish[act]/input.475
        self.module_192 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[97]/Conv2d[conv]/input.477
        self.module_193 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[97]/Hardswish[act]/input.481
        self.module_194 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[98]/Conv2d[conv]/input.483
        self.module_195 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[98]/Hardswish[act]/input.487
        self.module_196 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[99]/Conv2d[conv]/input.489
        self.module_197 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[99]/Hardswish[act]/12202
        self.module_198 = py_nndct.nn.Cat() #Model::Model/Concat[model]/Concat[100]/Cat[cat]/input.493
        self.module_199 = py_nndct.nn.Conv2d(in_channels=2048, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/Conv[model]/Conv[101]/Conv2d[conv]/input.495
        self.module_200 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/Conv[model]/Conv[101]/Hardswish[act]/input.503
        self.module_201 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/RepConv[model]/RepConv[102]/Conv2d[rbr_reparam]/input.499
        self.module_202 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/RepConv[model]/RepConv[102]/Hardswish[act]/input.507
        self.module_203 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/RepConv[model]/RepConv[103]/Conv2d[rbr_reparam]/input.501
        self.module_204 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/RepConv[model]/RepConv[103]/Hardswish[act]/input.509
        self.module_205 = py_nndct.nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Model::Model/RepConv[model]/RepConv[104]/Conv2d[rbr_reparam]/input.505
        self.module_206 = py_nndct.nn.Hardswish(inplace=False) #Model::Model/RepConv[model]/RepConv[104]/Hardswish[act]/input
        self.module_207 = py_nndct.nn.Conv2d(in_channels=256, out_channels=30, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/NNDctDetect[model]/NNDctDetect[105]/Conv2d[m]/ModuleList[0]/inputs.3
        self.module_208 = py_nndct.nn.dequant_output() #Model::Model/NNDctDetect[model]/NNDctDetect[105]/DeQuantStub[dequant]/ModuleList[0]/12311
        self.module_209 = py_nndct.nn.Conv2d(in_channels=512, out_channels=30, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/NNDctDetect[model]/NNDctDetect[105]/Conv2d[m]/ModuleList[1]/inputs.5
        self.module_210 = py_nndct.nn.dequant_output() #Model::Model/NNDctDetect[model]/NNDctDetect[105]/DeQuantStub[dequant]/ModuleList[1]/12333
        self.module_211 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=30, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/NNDctDetect[model]/NNDctDetect[105]/Conv2d[m]/ModuleList[2]/inputs
        self.module_212 = py_nndct.nn.dequant_output() #Model::Model/NNDctDetect[model]/NNDctDetect[105]/DeQuantStub[dequant]/ModuleList[2]/12355

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_0 = self.module_6(output_module_0)
        output_module_0 = self.module_7(output_module_0)
        output_module_0 = self.module_8(output_module_0)
        output_module_0 = self.module_9(output_module_0)
        output_module_10 = self.module_10(output_module_0)
        output_module_10 = self.module_11(output_module_10)
        output_module_12 = self.module_12(output_module_0)
        output_module_12 = self.module_13(output_module_12)
        output_module_14 = self.module_14(output_module_12)
        output_module_14 = self.module_15(output_module_14)
        output_module_14 = self.module_16(output_module_14)
        output_module_14 = self.module_17(output_module_14)
        output_module_18 = self.module_18(output_module_14)
        output_module_18 = self.module_19(output_module_18)
        output_module_18 = self.module_20(output_module_18)
        output_module_18 = self.module_21(output_module_18)
        output_module_18 = self.module_22(dim=1, tensors=[output_module_18,output_module_14,output_module_12,output_module_10])
        output_module_18 = self.module_23(output_module_18)
        output_module_18 = self.module_24(output_module_18)
        output_module_25 = self.module_25(output_module_18)
        output_module_25 = self.module_26(output_module_25)
        output_module_25 = self.module_27(output_module_25)
        output_module_28 = self.module_28(output_module_18)
        output_module_28 = self.module_29(output_module_28)
        output_module_28 = self.module_30(output_module_28)
        output_module_28 = self.module_31(output_module_28)
        output_module_28 = self.module_32(dim=1, tensors=[output_module_28,output_module_25])
        output_module_33 = self.module_33(output_module_28)
        output_module_33 = self.module_34(output_module_33)
        output_module_35 = self.module_35(output_module_28)
        output_module_35 = self.module_36(output_module_35)
        output_module_37 = self.module_37(output_module_35)
        output_module_37 = self.module_38(output_module_37)
        output_module_37 = self.module_39(output_module_37)
        output_module_37 = self.module_40(output_module_37)
        output_module_41 = self.module_41(output_module_37)
        output_module_41 = self.module_42(output_module_41)
        output_module_41 = self.module_43(output_module_41)
        output_module_41 = self.module_44(output_module_41)
        output_module_41 = self.module_45(dim=1, tensors=[output_module_41,output_module_37,output_module_35,output_module_33])
        output_module_41 = self.module_46(output_module_41)
        output_module_41 = self.module_47(output_module_41)
        output_module_48 = self.module_48(output_module_41)
        output_module_48 = self.module_49(output_module_48)
        output_module_48 = self.module_50(output_module_48)
        output_module_51 = self.module_51(output_module_41)
        output_module_51 = self.module_52(output_module_51)
        output_module_51 = self.module_53(output_module_51)
        output_module_51 = self.module_54(output_module_51)
        output_module_51 = self.module_55(dim=1, tensors=[output_module_51,output_module_48])
        output_module_56 = self.module_56(output_module_51)
        output_module_56 = self.module_57(output_module_56)
        output_module_58 = self.module_58(output_module_51)
        output_module_58 = self.module_59(output_module_58)
        output_module_60 = self.module_60(output_module_58)
        output_module_60 = self.module_61(output_module_60)
        output_module_60 = self.module_62(output_module_60)
        output_module_60 = self.module_63(output_module_60)
        output_module_64 = self.module_64(output_module_60)
        output_module_64 = self.module_65(output_module_64)
        output_module_64 = self.module_66(output_module_64)
        output_module_64 = self.module_67(output_module_64)
        output_module_64 = self.module_68(dim=1, tensors=[output_module_64,output_module_60,output_module_58,output_module_56])
        output_module_64 = self.module_69(output_module_64)
        output_module_64 = self.module_70(output_module_64)
        output_module_71 = self.module_71(output_module_64)
        output_module_71 = self.module_72(output_module_71)
        output_module_71 = self.module_73(output_module_71)
        output_module_74 = self.module_74(output_module_64)
        output_module_74 = self.module_75(output_module_74)
        output_module_74 = self.module_76(output_module_74)
        output_module_74 = self.module_77(output_module_74)
        output_module_74 = self.module_78(dim=1, tensors=[output_module_74,output_module_71])
        output_module_79 = self.module_79(output_module_74)
        output_module_79 = self.module_80(output_module_79)
        output_module_81 = self.module_81(output_module_74)
        output_module_81 = self.module_82(output_module_81)
        output_module_83 = self.module_83(output_module_81)
        output_module_83 = self.module_84(output_module_83)
        output_module_83 = self.module_85(output_module_83)
        output_module_83 = self.module_86(output_module_83)
        output_module_87 = self.module_87(output_module_83)
        output_module_87 = self.module_88(output_module_87)
        output_module_87 = self.module_89(output_module_87)
        output_module_87 = self.module_90(output_module_87)
        output_module_87 = self.module_91(dim=1, tensors=[output_module_87,output_module_83,output_module_81,output_module_79])
        output_module_87 = self.module_92(output_module_87)
        output_module_87 = self.module_93(output_module_87)
        output_module_94 = self.module_94(output_module_87)
        output_module_94 = self.module_95(output_module_94)
        output_module_94 = self.module_96(output_module_94)
        output_module_94 = self.module_97(output_module_94)
        output_module_94 = self.module_98(output_module_94)
        output_module_94 = self.module_99(output_module_94)
        output_module_100 = self.module_100(output_module_94)
        output_module_101 = self.module_101(output_module_94)
        output_module_102 = self.module_102(output_module_94)
        output_module_103 = self.module_103(dim=1, tensors=[output_module_94,output_module_100,output_module_101,output_module_102])
        output_module_103 = self.module_104(output_module_103)
        output_module_103 = self.module_105(output_module_103)
        output_module_103 = self.module_106(output_module_103)
        output_module_103 = self.module_107(output_module_103)
        output_module_108 = self.module_108(output_module_87)
        output_module_108 = self.module_109(output_module_108)
        output_module_103 = self.module_110(dim=1, tensors=[output_module_103,output_module_108])
        output_module_103 = self.module_111(output_module_103)
        output_module_103 = self.module_112(output_module_103)
        output_module_113 = self.module_113(output_module_103)
        output_module_113 = self.module_114(output_module_113)
        output_module_113 = self.module_115(input=output_module_113, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_116 = self.module_116(output_module_64)
        output_module_116 = self.module_117(output_module_116)
        output_module_116 = self.module_118(dim=1, tensors=[output_module_116,output_module_113])
        output_module_119 = self.module_119(output_module_116)
        output_module_119 = self.module_120(output_module_119)
        output_module_121 = self.module_121(output_module_116)
        output_module_121 = self.module_122(output_module_121)
        output_module_123 = self.module_123(output_module_121)
        output_module_123 = self.module_124(output_module_123)
        output_module_125 = self.module_125(output_module_123)
        output_module_125 = self.module_126(output_module_125)
        output_module_127 = self.module_127(output_module_125)
        output_module_127 = self.module_128(output_module_127)
        output_module_129 = self.module_129(output_module_127)
        output_module_129 = self.module_130(output_module_129)
        output_module_129 = self.module_131(dim=1, tensors=[output_module_129,output_module_127,output_module_125,output_module_123,output_module_121,output_module_119])
        output_module_129 = self.module_132(output_module_129)
        output_module_129 = self.module_133(output_module_129)
        output_module_134 = self.module_134(output_module_129)
        output_module_134 = self.module_135(output_module_134)
        output_module_134 = self.module_136(input=output_module_134, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_137 = self.module_137(output_module_41)
        output_module_137 = self.module_138(output_module_137)
        output_module_137 = self.module_139(dim=1, tensors=[output_module_137,output_module_134])
        output_module_140 = self.module_140(output_module_137)
        output_module_140 = self.module_141(output_module_140)
        output_module_142 = self.module_142(output_module_137)
        output_module_142 = self.module_143(output_module_142)
        output_module_144 = self.module_144(output_module_142)
        output_module_144 = self.module_145(output_module_144)
        output_module_146 = self.module_146(output_module_144)
        output_module_146 = self.module_147(output_module_146)
        output_module_148 = self.module_148(output_module_146)
        output_module_148 = self.module_149(output_module_148)
        output_module_150 = self.module_150(output_module_148)
        output_module_150 = self.module_151(output_module_150)
        output_module_150 = self.module_152(dim=1, tensors=[output_module_150,output_module_148,output_module_146,output_module_144,output_module_142,output_module_140])
        output_module_150 = self.module_153(output_module_150)
        output_module_150 = self.module_154(output_module_150)
        output_module_155 = self.module_155(output_module_150)
        output_module_155 = self.module_156(output_module_155)
        output_module_155 = self.module_157(output_module_155)
        output_module_158 = self.module_158(output_module_150)
        output_module_158 = self.module_159(output_module_158)
        output_module_158 = self.module_160(output_module_158)
        output_module_158 = self.module_161(output_module_158)
        output_module_158 = self.module_162(dim=1, tensors=[output_module_158,output_module_155,output_module_129])
        output_module_163 = self.module_163(output_module_158)
        output_module_163 = self.module_164(output_module_163)
        output_module_165 = self.module_165(output_module_158)
        output_module_165 = self.module_166(output_module_165)
        output_module_167 = self.module_167(output_module_165)
        output_module_167 = self.module_168(output_module_167)
        output_module_169 = self.module_169(output_module_167)
        output_module_169 = self.module_170(output_module_169)
        output_module_171 = self.module_171(output_module_169)
        output_module_171 = self.module_172(output_module_171)
        output_module_173 = self.module_173(output_module_171)
        output_module_173 = self.module_174(output_module_173)
        output_module_173 = self.module_175(dim=1, tensors=[output_module_173,output_module_171,output_module_169,output_module_167,output_module_165,output_module_163])
        output_module_173 = self.module_176(output_module_173)
        output_module_173 = self.module_177(output_module_173)
        output_module_178 = self.module_178(output_module_173)
        output_module_178 = self.module_179(output_module_178)
        output_module_178 = self.module_180(output_module_178)
        output_module_181 = self.module_181(output_module_173)
        output_module_181 = self.module_182(output_module_181)
        output_module_181 = self.module_183(output_module_181)
        output_module_181 = self.module_184(output_module_181)
        output_module_181 = self.module_185(dim=1, tensors=[output_module_181,output_module_178,output_module_103])
        output_module_186 = self.module_186(output_module_181)
        output_module_186 = self.module_187(output_module_186)
        output_module_188 = self.module_188(output_module_181)
        output_module_188 = self.module_189(output_module_188)
        output_module_190 = self.module_190(output_module_188)
        output_module_190 = self.module_191(output_module_190)
        output_module_192 = self.module_192(output_module_190)
        output_module_192 = self.module_193(output_module_192)
        output_module_194 = self.module_194(output_module_192)
        output_module_194 = self.module_195(output_module_194)
        output_module_196 = self.module_196(output_module_194)
        output_module_196 = self.module_197(output_module_196)
        output_module_196 = self.module_198(dim=1, tensors=[output_module_196,output_module_194,output_module_192,output_module_190,output_module_188,output_module_186])
        output_module_196 = self.module_199(output_module_196)
        output_module_196 = self.module_200(output_module_196)
        output_module_201 = self.module_201(output_module_150)
        output_module_201 = self.module_202(output_module_201)
        output_module_203 = self.module_203(output_module_173)
        output_module_203 = self.module_204(output_module_203)
        output_module_196 = self.module_205(output_module_196)
        output_module_196 = self.module_206(output_module_196)
        output_module_201 = self.module_207(output_module_201)
        output_module_201 = self.module_208(input=output_module_201)
        output_module_203 = self.module_209(output_module_203)
        output_module_203 = self.module_210(input=output_module_203)
        output_module_196 = self.module_211(output_module_196)
        output_module_196 = self.module_212(input=output_module_196)
        return (output_module_201,output_module_203,output_module_196)
