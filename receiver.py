import cv2
import numpy as np
import socket
import os
import time
from collections import deque
import threading

# -- 設定 --
UDP_IP = "127.0.0.1"      # 監聽本地主機
UDP_PORT = 8008           # 必須與 sender.py 的通訊埠相同
MAX_PACKET_SIZE = 65507   # UDP 封包大小上限
END_SIGNAL = b"__END__"   # 傳輸結束信號
FPS = 10                  # 播放速率
BUFFER_SIZE = 10          # 緩衝區大小，存到 10 張就開始播

# -- 全域變數 --
image_buffer = deque() # 使用雙向佇列作為圖片緩衝區
stop_event = threading.Event() # 用於通知執行緒停止的事件

def receive_thread():
    """在背景執行緒中接收圖片"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"接收執行緒啟動，正在監聽 {UDP_IP}:{UDP_PORT}...")

    while not stop_event.is_set():
        try:
            # 設定超時，這樣迴圈可以定期檢查 stop_event
            sock.settimeout(1.0)
            
            # 1. 接收檔名或結束信號
            data, addr = sock.recvfrom(4096)
            
            if data == END_SIGNAL:
                print("接收執行緒：收到結束信號。")
                break
            
            filename = data.decode()
            
            # 2. 接收檔案大小
            size_data, addr = sock.recvfrom(1024)
            size = int(size_data.decode())

            # 3. 接收檔案資料
            img_data = b''
            while len(img_data) < size:
                chunk, addr = sock.recvfrom(MAX_PACKET_SIZE)
                img_data += chunk
            
            if len(img_data) == size:
                # 解碼圖片並加入緩衝區
                frame = cv2.imdecode(np.frombuffer(img_data, dtype=np.uint8), 1)
                if frame is not None:
                    image_buffer.append(frame)
                    print(f"已接收 {filename}，目前緩衝區大小: {len(image_buffer)}")
                # 4. 回傳 ACK
                sock.sendto(b'ACK_FILE_RECEIVED', addr)
            else:
                sock.sendto(b'ACK_FILE_FAILED', addr)

        except socket.timeout:
            continue # 超時是正常的，繼續檢查 stop_event
        except Exception as e:
            print(f"接收執行緒發生錯誤: {e}")
            
    sock.close()
    print("接收執行緒結束。")

def main():
    # 啟動背景接收執行緒
    receiver = threading.Thread(target=receive_thread)
    receiver.daemon = True
    receiver.start()

    window_name = "直播串流"
    print("主執行緒：等待緩衝區達到 10 張圖片...")

    # 等待緩衝區填滿
    while len(image_buffer) < BUFFER_SIZE:
        if not receiver.is_alive() and not image_buffer:
             print("接收執行緒已停止且緩衝區為空，無法播放。")
             return
        time.sleep(0.5)

    print("緩衝區已滿，開始播放！")

    while True:
        if image_buffer:
            frame = image_buffer.popleft()
            cv2.imshow(window_name, frame)
            
            if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('q'):
                print("使用者按下 'q'，準備結束...")
                break
        elif not receiver.is_alive():
            # 如果緩衝區空了，且接收執行緒也結束了，就退出播放
            print("播放完畢。")
            break
        else:
            # 緩衝區空了，但還在接收，稍微等待
            time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n使用者中斷程式。")
    finally:
        stop_event.set() # 通知接收執行緒停止
        cv2.destroyAllWindows()
        print("所有視窗已銷毀。")