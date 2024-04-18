'''
    For getting srt file from any video.
'''
import os
import sys

from dotenv import load_dotenv
import openai


def get_srt(src_file, dst_path, response_format="srt"):
    '''
        Get srt file from video.
        Args:
            src_file: str, source file path.
            dst_path: str, destination path.
            response_format: str, format of the response.
        Returns:
            None

        CLI Example:
            python srt_getter.py "path/to/source/file" "path/to/destination"
    '''
    # get api key from environment variables
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_WHISPER_API_KEY")

    # get file from src_file and transcribe it
    with open(src_file, "rb") as audio_file:
        result = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file,
            response_format=response_format,
            prompt='請使用繁體中文文字產出字幕。',
        )
        with open(f"{dst_path}/output.srt", "w", encoding="utf-8") as f:
            f.write(result)


if __name__ == "__main__":
    try:
        # 開始執行提示
        print(f"Start to get srt file from {sys.argv[1]}...")
        # 從 system argument 取得檔案路徑
        src_file_demo = sys.argv[1]
        dst_path_demo = sys.argv[2]
        # 執行 get_srt()
        get_srt(src_file_demo, dst_path_demo)
        # 印出成功訊息
        print(f"Success!, srt file is saved in {dst_path_demo}/output.srt")
    except Exception as e:
        # 印出錯誤訊息
        print(f"Error: {e}")
        # 結束程式
        sys.exit(1)
