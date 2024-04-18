# videoTranslater for Windows 10/11

A video transcriptor with OpenAI Whisper api for Windows 10/11.

## 基本需求

取得原影片語音轉文字內容之字幕，可由 Whisper api 取得語音辨識結果。
結合原影片與英文版配音，透過 ffmpeg 結合影片與音訊。

## 目前版本使用說明

1. 於電腦中安裝 [FFmpeg](https://ffmpeg.org/download.html#build-windows)。
2. 於電腦中安裝 [Python](https://www.python.org/downloads/)。
3. 下載此 Repository 至本機端。
    * 使用 git。

        ```bash
        # execute in PowerShell
        > git clone https://github.com/gandolfreddy/videoTranscriptor.git
        ```

4. 於 [OpenAI](https://platform.openai.com/account/api-keys) 網站中，申請一組 API Key。
5. 於下載後的專案目錄中，新增一個名為 `.env` 的檔案，內容填入 `OPENAI_WHISPER_API_KEY='此處填入申請的 API Key'`。
6. 於專案目錄中開啟命令提示列介面（或於命令提示列介面中，將操作的目錄調整至專案目錄），執行以下命令，用以安裝需要的模組／套件。

    ```bash
    # execute in PowerShell
    > pip install -r requirements.txt
    ```

7. 成功安裝後，便可開始使用此工具。
    * 首先於命令提示列介面中，將操作的目錄調整至專案目錄。

        ```bash
        # execute in PowerShell
        > cd "C:\Users\me\Desktop\videoTranscriptor"
        ```

    * 將超過特定檔案大小（25MB）的檔案進行壓縮，利用 `ffmpeg` 進行壓縮。

        ```bash
        # execute in PowerShell
        > ffmpeg -i <video file> -b:v 128K <output_video file>
        # e.g.
        > ffmpeg -i "C:/Users/me/Desktop/videos/video_2024_04_01.mp4" -b:v 128K "C:/Users/me/Desktop/videos/video_2024_04_01_compressed.mp4"
        ```

    * 基本使用方式：執行以下命令，即可取出指定的中文影片字幕（檔案大小需小於 25 MB）。

        ```bash
        # execute in PowerShell
        > python srt_getter.py <原影片位置> <欲存放字幕檔的存放位置>
        # e.g.
        > python srt_getter.py "C:/Users/me/Desktop/videos/video_2024_04_01.mp4" "C:/Users/me/Desktop/srt/"
        ```

## 相關工具

* [Clipchamp](https://app.clipchamp.com/)
* [Download FFmpeg](https://ffmpeg.org/download.html#build-windows)

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
