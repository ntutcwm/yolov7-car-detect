import os 

# --- 修改從這裡開始 ---

# 1. 定義你的專案根目錄 (你執行腳本的地方)
#    os.path.abspath(os.path.curdir) 會自動取得目前的工作目錄，更具彈性
#    或者你也可以寫死：project_root = "/home/aero602/Vitis-AI-3.0/yolov7_VitisAI-main-quant+main/yolov7_VitisAI-main"
project_root = os.getcwd() # getcwd() = get current working directory

# 2. 定義你要讀取圖片的 "絕對路徑"
#    這樣 os.listdir() 才能正確找到檔案
abs_test_base_path = os.path.join(project_root, "dataset", "test", "images")


# --- 後續的設定不變 ---
sampling_rate = 10
output_filepath = os.path.join(project_root, "dataset", "test-q.txt") 

# 自動建立輸出目錄
output_dir = os.path.dirname(output_filepath)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files_written_count = 0
with open(output_filepath, "w", encoding="utf-8") as f:
    # 注意：listdir 要用 "絕對路徑" 去讀取
    try:
        img_list = os.listdir(abs_test_base_path)
    except FileNotFoundError:
        print(f"錯誤：找不到圖片目錄 {abs_test_base_path}")
        print("請確認你的腳本是從專案根目錄執行的，或者手動修改 project_root 變數。")
        exit() # 找不到檔案就直接結束程式

    img_list.sort()
    
    for index, fname in enumerate(img_list):
        if index % sampling_rate == 0:
            # 取得圖片的完整絕對路徑
            abs_file_path = os.path.join(abs_test_base_path, fname)
            
            # 3. 計算相對於 "專案根目錄" 的 "相對路徑"
            relative_path = os.path.relpath(abs_file_path, project_root)
            
            # 在Linux系統上，路徑分隔符是'/'，可以手動替換以確保一致性
            relative_path = relative_path.replace(os.sep, '/')

            # 4. 將 "相對路徑" 寫入檔案
            f.write(relative_path + "\n")
            files_written_count += 1

print(f"取樣完成！已將 {files_written_count} 個【相對路徑】寫入到 {output_filepath}")