import replicate
from dotenv import load_dotenv
import os

load_dotenv()

class WhisperService:
    def __init__(self):
        self.client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
        
    def transcribe(self, audio_file: str) -> str:
        response = self.client.run(
                "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c",
                input={
                    "audio": open(audio_file, "rb"),
                    "language": "spanish",
                    "task": "transcribe",
                    "timestamp": "chunk",
                }
        )
        return response
