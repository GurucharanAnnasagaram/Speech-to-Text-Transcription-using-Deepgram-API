import os
from dotenv import load_dotenv

load_dotenv()
from deepgram import (DeepgramClient, PrerecordedOptions, FileSource, )

API_KEY = os.getenv("DQ_API_KEY")


def speech2text(audio_input):
    try:
        deepgram = DeepgramClient(API_KEY)
        with open(audio_input, "rb") as file:
            buffer_data = file.read()
        payload: FileSource = {
            "buffer": buffer_data,
        }
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True
        )
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        print(response)
        print(response["results"]["channels"][0]["alternatives"][0]["transcript"])
        return response["results"]["channels"][0]["alternatives"][0]["transcript"]
    except Exception as e:
        print(f"Exception : {e}")


if __name__ == "__main__":
    speech2text("voice.mp3")
