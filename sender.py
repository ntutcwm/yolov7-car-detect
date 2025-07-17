import socket
import os
import time
import glob

# -- 設定 --
UDP_IP = "127.0.0.1"      # 本地測試 IP 位址
UDP_PORT = 8008           # 必須與 receiver.py 的通訊埠相同
IMAGE_DIR = "result"      # 圖片資料夾
FPS = 10                  # 每秒傳送的目標速率
MAX_PACKET_SIZE = 65507   # UDP 封包大小上限
END_SIGNAL = b"__END__"   # 傳輸結束信號

# -- 初始化 --
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5) # 設定 5 秒超時

def send_file(filepath):
    """傳送單一檔案並等待最終 ACK"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"找不到檔案: {filepath}")
        return False

    filename = os.path.basename(filepath)
    size = len(data)
    
    print(f"正在傳送 {filename} ({size} bytes)...")

    # 1. 傳送檔名
    sock.sendto(filename.encode(), (UDP_IP, UDP_PORT))
    
    # 2. 傳送檔案大小
    sock.sendto(str(size).encode(), (UDP_IP, UDP_PORT))

    # 3. 分割並傳送檔案資料
    for i in range(0, size, MAX_PACKET_SIZE):
        chunk = data[i:i+MAX_PACKET_SIZE]
        sock.sendto(chunk, (UDP_IP, UDP_PORT))
        time.sleep(0.001) # 每個 chunk 間極短延遲，避免衝擊緩衝區
    
    # 4. 等待此檔案的最終 ACK
    ack, addr = sock.recvfrom(1024)
    if ack == b'ACK_FILE_RECEIVED':
        print(f"已傳送: {filename} (收到 ACK)")
        return True
    else:
        print(f"收到無效的 ACK: {ack}")
        return False

def main():
    image_files = sorted(glob.glob(os.path.join(IMAGE_DIR, '*.jpg')))
    if not image_files:
        print(f"在 '{IMAGE_DIR}' 資料夾中找不到任何 .jpg 檔案。")
        return

    print(f"找到 {len(image_files)} 個圖片檔案。準備開始傳輸...")
    
    for filepath in image_files:
        try:
            if send_file(filepath):
                # 成功傳送後，根據 FPS 控制速率
                time.sleep(1/FPS)
            else:
                print(f"檔案 {os.path.basename(filepath)} 傳送失敗。")
                break
        except socket.timeout:
            print(f"錯誤: 等待 {os.path.basename(filepath)} 的 ACK 超時。中止傳輸。")
            break
    
    print("所有檔案傳輸流程完畢。傳送結束信號。")
    sock.sendto(END_SIGNAL, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n使用者中斷程式。")
    finally:
        sock.close()
        print("Socket 已關閉。")