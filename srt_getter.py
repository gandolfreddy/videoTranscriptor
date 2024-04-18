'''
    For getting srt file from any video.
'''
import os

from dotenv import load_dotenv
import openai


def get_srt(src_file, dst_path, language="zh", response_format="srt"):
    '''
        Get srt file from video.
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
            language=language,
        )
        with open(f"{dst_path}/output.srt", "w", encoding="utf-8") as f:
            f.write(result)
