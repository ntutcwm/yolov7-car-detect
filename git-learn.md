# 將本地專案上傳到 GitHub 教學

本教學將引導您完成將本地專案上傳到 GitHub 的完整流程，包括初始化 Git 儲存庫、處理大檔案問題以及成功推送到遠端。

## 步驟 1：初始化本地 Git 儲存庫

首先，在您的專案根目錄中初始化一個新的 Git 儲存庫。

```bash
git init
```

## 步驟 2：將本地儲存庫與遠端 GitHub 儲存庫連結

接著，將您的本地儲存庫與您在 GitHub 上建立的遠端儲存庫連結起來。

```bash
git remote add origin https://github.com/ntutcwm/yolov7-car-detect.git
```
*   `origin` 是您遠端儲存庫的預設名稱。
*   請將 URL 替換為您自己的 GitHub 儲存庫 URL。

## 步驟 3：將所有檔案加入並建立第一個 Commit

將專案中的所有檔案加入到 Git 的暫存區，然後建立一個 commit 來記錄這些變更。

```bash
git add .
git commit -m "Initial commit of YOLOv7 project"
```

**`git add .` vs `git add <檔案名稱>` 的差別：**

*   **`git add .`**: 這個指令會將**目前目錄下所有**的變更（包括新增的檔案和修改過的檔案）都加入到暫存區。`.` 代表「目前目錄」。這是一個快速將所有變更一次加入的好方法。

*   **`git add <檔案名稱>`**: 這個指令只會將您**指定的那個檔案**加入到暫存區。如果您只想提交一部分檔案的變更，這個指令就很有用。您也可以指定一個目錄路徑，例如 `git add utils/`，來加入整個 `utils` 目錄下的所有變更。

總結來說，當您想要一次提交所有變更時，使用 `git add .`；當您只想提交特定幾個檔案的變更時，就使用 `git add <檔案名稱>`。

*   `-m` 是 "message" 的縮寫，這個選項讓您可以直接在指令後面提供一段簡短的 commit 訊息。每一筆 commit 都應該要有一段訊息，用來描述這次的變更內容。
如果沒有使用 -m 選項，Git 會自動開啟一個文字編輯器（例如 Vim 或 Nano），讓您輸入 commit 訊息。
## 步驟 4：推送到 GitHub (首次嘗試與問題排解)

現在，嘗試將您的 commit 推送到 GitHub。

```bash
git push origin master
```

**可能遇到的問題：大檔案錯誤**

如果您在推送時遇到類似以下的錯誤訊息，代表您的專案中包含超過 GitHub 限制 (通常是 100MB) 的大檔案。

```
remote: error: File yolov7.pt is 72.09 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: error: File dataset/tesi.v3i.yolov7pytorch.zip is 596.72 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
```

**解決方案：**

通常，我們不會將模型權重檔 (`.pt`) 或大型資料集 (`.zip`) 等檔案直接上傳到 Git。最好的方法是使用 `.gitignore` 檔案來忽略它們。

### 4.1 更新 `.gitignore`

編輯專案根目錄下的 `.gitignore` 檔案，將大檔案的路徑加入其中。

```
# Large files
yolov7.pt
dataset/tesi.v3i.yolov7pytorch.zip
```

### 4.2 從 Git 追蹤中移除大檔案

更新 `.gitignore` 後，您需要從 Git 的索引中移除這些檔案（這不會刪除您本地的檔案）。

```bash
git rm --cached yolov7.pt
git rm --cached dataset/tesi.v3i.yolov7pytorch.zip
```

### 4.3 修改上一個 Commit

因為我們已經將大檔案從 Git 中移除，所以需要更新上一個 commit 來反映這個變更。`--amend` 選項可以讓我們修改最後一個 commit。

```bash
git commit --amend --no-edit
```
*   `--no-edit` 表示我們不想修改 commit 訊息。

## 步驟 5：強制推送到 GitHub

由於我們修改了 commit 歷史紀錄，因此需要使用 `--force` (或 `-f`) 選項來強制推送更新到 GitHub。

**警告：** 強制推送會覆蓋遠端儲存庫的歷史紀錄。在協作專案中請謹慎使用。但在這種初始化儲存庫的情況下，這是安全的。

```bash
git push --force origin master
```

執行此指令後，您的專案應該已成功上傳到 GitHub，且不再包含那些大檔案。