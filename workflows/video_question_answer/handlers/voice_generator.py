from services import ElevenLabsService

class VoiceGenerator:
    def __init__(self):
        self.client = ElevenLabsService()

    def generate_voice(self, text: str):
        return self.client.generate_voice(text)
