from services.openai_service import OpenAIService
from services.deepseek_service import DeepSeekService

class AnimationFixerHandler:
    def __init__(self):
        self.openai_service = DeepSeekService()
        self.system_prompt = """
        Eres un experto programador especializado en depurar y corregir código de animaciones educativas usando la biblioteca Manim de Python.
        Responde únicamente con el código corregido, sin ningún comentario o explicación adicional.
        Busca principalmente errores del tipo:
        - LaTeX compilation error: Missing $ inserted. 
        - LaTeX compilation error: Undefined control sequence. 
        - LaTeX compilation error: Missing } inserted 
        - No debes usar TexFontTemplate
        
                      """

    def fix_animation_code(self, code):
        response = self.openai_service.chat_completion(
            system_prompt=self.system_prompt,
            user_prompt=code
        )
        return response