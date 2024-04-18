# videoSpeechTranslater for Windows 10/11
A speech translater for video with OpenAI Whisper api for Windows 10/11.

## 基本需求
- [x] 1. 取得原影片語音轉文字內容之字幕。
    > 可由 Whisper api 取得語音辨識結果並翻譯。 
- [x] 2. 取得字幕的翻譯（中翻英）。
    > 可由 Whisper api 取得語音辨識結果並翻譯。 
- [x] 3. 取得英文版字幕的配音語音。
    > 透過 `edge-srt-to-speech` 取得可接受配音。
- [x] 4. 結合原影片與英文版配音。
    > 透過 ffmpeg 取得靜音影片，並透過 ffmpeg 結合靜音影片與音訊。 

## 目前版本使用說明
1. 於電腦中安裝 [FFmpeg](https://ffmpeg.org/download.html#build-windows)。
2. 於電腦中安裝 [Python](https://www.python.org/downloads/)。
3. 下載此 Repository 至本機端。
    * 使用 git。
        ```bash
        # execute in PowerShell
        > git clone https://github.com/gandolfreddy/videoSpeechTranslater.git
        ```
    * 下載壓縮檔。

        ![image](https://github.com/gandolfreddy/videoSpeechTranslater/assets/22278312/2f85cacf-eef2-4193-9178-ab8c130f62cb)
        
3. 於 [OpenAI](https://platform.openai.com/account/api-keys) 網站中，申請一組 API Key。
4. 於下載後的專案目錄中，新增一個名為 `.env` 的檔案，內容填入 `OPENAI_WHISPER_API_KEY='此處填入申請的 API Key'`。
    ![image](https://github.com/gandolfreddy/videoSpeechTranslater/assets/22278312/23b856c0-5880-4e12-9d79-ed7b3beb4d49)
    
5. 於專案目錄中開啟命令提示列介面（或於命令提示列介面中，將操作的目錄調整至專案目錄），執行以下命令，用以安裝需要的模組／套件。
    ```bash
    # execute in PowerShell
    > pip install -r requirements.txt
    ```
6. 成功安裝後，便可開始使用此工具。
    * 基本使用方式：執行以下命令，即可將指定的中文影片（檔案大小需小於 25 MB），轉換成英文配音影片。
        ```bash
        # execute in PowerShell
        > python vst.py -s <欲轉換成英文的中文影片存放位置>
        # e.g.
        > python vst.py -s C:\Users\me\Desktop\src_video\a.mp4
        ```
    * 相關參數說明。
        |參數|說明|
        |---|---|
        |`-h`, `--help` | 顯示此說明訊息並退出。 |
        |`-s SRC_PATH`, `--src-path SRC_PATH` | 來源影片的路徑，例如 `C:\Users\me\Desktop\src_video\a.mp4`。 |
        |`-sp SRT_PATH`, `--srt-path SRT_PATH` | srt 檔案的資料夾路徑，例如 `srt/`。預設值：`$home/Desktop/material_dir_[yyyymmdd]`。 |
        |`-ap AUDIO_PATH`, `--audio-path AUDIO_PATH` | 音訊檔案的資料夾路徑，例如 `audio/`。預設值：`$home/Desktop/material_dir_[yyyymmdd]`。 |
        |`-mvp MUTED_VIDEO_PATH`, `--muted-video-path MUTED_VIDEO_PATH` | 無聲影片檔案的資料夾路徑，例如 `muted_video/`。預設值：`$home/Desktop/material_dir_[yyyymmdd]`。 |
        |`-dp DST_PATH`, `--dst-path DST_PATH` | 目標影片檔案的資料夾路徑，例如 `dst/`。預設值：`$home/Desktop/material_dir_[yyyymmdd]`。 |
    * 範例。
        * 不指定其餘參數，僅給來源影片路徑，則此工具會在桌面建立以 `material_dir_[yyyymmdd]` 命名的資料夾，其中 `[yyyymmdd]` 表當天日期。
            ```bash
            # execute in PowerShell
            > python vst.py -s C:\Users\me\Desktop\src_video\a.mp4
            ```
        * 指定 `-dp` 參數，則影片輸出結果，將會存放於 `C:\Users\me\Desktop\dst\` 資料夾中。
            ```bash
            # execute in PowerShell
            > python vst.py -s C:\Users\me\Desktop\src_video\a.mp4 -dp C:\Users\me\Desktop\dst\
            ```
        * 指定 `-sp` 參數，則來源影片的英文翻譯字幕檔，將會存放於 `C:\Users\me\Desktop\srt\` 資料夾中。
            ```bash
            # execute in PowerShell
            > python vst.py -s C:\Users\me\Desktop\src_video\a.mp4 -sp C:\Users\me\Desktop\srt\
            ```


## 實驗記錄
### 取得原影片語音轉文字內容之字幕，並取得字幕的翻譯（中翻英）。
* 安裝 `openai` 與 `dotenv` 模組。
    ```bash
    # execute in PowerShell
    > pip install openai
    > pip install python-dotenv
    ```
* 設定 OpenAI API Key。
    ```python
    openai.api_key = os.getenv('設定 API KEY 的環境變數')
    ```
* 取得 `file_path` 影像檔案的字幕（`.srt`）並翻譯成英文，最後輸出至 `srts/en_out.srt`。
    ```python
    file_path = '存放影像檔案的目錄路徑'
    with open(file_path, "rb") as audio_file:
        transcription = openai.Audio.translate(
            model="whisper-1",
            file=audio_file,
            response_format="srt",
            language="en",
        )
        with open(f"srts/en_out.srt", "w", encoding="utf-8") as f:
            f.write(transcription)
    ```
### 取得英文版字幕的配音語音。
* 安裝 `edge-srt-to-speech` 模組。
    ```bash
    # execute in PowerShell
    > pip install edge-srt-to-speech
    ```
* 透過 `edge-srt-to-speech` 取得可接受配音。
    ```bash
    # execute in PowerShell
    > edge-srt-to-speech <srt file> <output_audio file> [--voice=<voice name>] [--default-speed<=[+-][0-100]%>]
    ```
### 結合原影片與英文版配音。
* 取得去除聲音版本的影像檔（CLI）。
    ```bash
    # execute in PowerShell
    > ffmpeg -i <video file> -vcodec copy -an <muted video file>
    ```
* 結合靜音影像檔與英文版配音（CLI）。
    ```bash
    # execute in PowerShell
    > ffmpeg -i <muted video file> -i <audio file> -c:v copy -c:a aac <output_video file> -shortest
    ```

## <span style="color: red;">實驗結果</span>
- 此流程基本可動作，**但於最後產出影片中，有部份音訊因受到字幕檔時間限制，讀文字的速度較快**，直接使用恐較不符合預期，需要靠後期精修處理。

## 相關工具
- [Clipchamp](https://app.clipchamp.com/)
- [Download FFmpeg](https://ffmpeg.org/download.html#build-windows)
- [rany2/edge-srt-to-speech](https://github.com/rany2/edge-srt-to-speech)
- [rany2/edge-tts](https://github.com/rany2/edge-tts)

## 參考資源
1. [Speech to text - OpenAI document](https://platform.openai.com/docs/guides/speech-to-text)
2. [[ChatGPT] 如何使用Whisper API 與 ChatGPT API 快速摘要YouTube 影片?](https://youtu.be/uD5_pKbBhgo)
3. [Getting Started With OpenAI Whisper API In Python | Beginner Tutorial](https://youtu.be/BkcSJol59Rg)
4. [AI上廣東話字幕免費（接近） | Cantonese subtitle generator | Python 教學 廣東話 | Whisper API](https://youtu.be/04bgLwKjCmY)
5. [appfromape/open_ai_whisper_1_transcribe](https://github.com/appfromape/open_ai_whisper_1_transcribe)
6. [openai/openai-cookbook](https://github.com/openai/openai-cookbook)
7. [( Day 18 ) 取出影片聲音、影片加入聲音](https://ithelp.ithome.com.tw/articles/10292945?sc=rss.qu)
8. [Subtitles to speech converter](https://voicenotebook.com/srtspeaker.php)
9. [Documentation - FFmpeg](https://www.ffmpeg.org/documentation.html)
10. [使用 ffmpeg 移除影片中的聲音 @ Windows](https://blog.changyy.org/2013/08/ffmpeg-windows.html)
11. [影音剪輯 / 使用 ffmpeg 指令合併影片及聲音檔 (直接複製資料不重新編碼)](https://note.charlestw.com/merging-video-and-audio-in-ffmpeg/)
12. [ffmpeg-python 0.2.0](https://pypi.org/project/ffmpeg-python/)
13. [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)
