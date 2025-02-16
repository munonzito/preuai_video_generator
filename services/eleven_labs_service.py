from elevenlabs.client import ElevenLabs
from elevenlabs import play, save

class ElevenLabsService:
    def __init__(self):
        self.client =  ElevenLabs()

    def generate_voice(self, text: str):
        audio = self.client.text_to_speech.convert(
            text=text,
            voice_id="JZISI4B0lik6Kitz5vi7",
            # model_id="eleven_multilingual_v2.5",
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128"
        )

        return audio
