from services.openai_service import OpenAIService
from services.deepseek_service import DeepSeekService

class ScriptGenerator:
    def __init__(self):
        self.client = DeepSeekService()
        self.system_prompt = """
        Eres un experto en crear guiones para videos de matemáticas.
        El usuario te proporcionará una solución paso a paso de una pregunta de matemáticas y un código de animación.
        Tu objetivo es crear un guion que esté alineado con el código de animación y que muestre el proceso paso a paso de la solución de la pregunta.
        
        Debes responder únicamente con el guión, el cual debe ser solamente lo que se narrará. No agregues acotaciones, comentarios o explicaciones.
        El guión debe ser directo, comenzando con el enunciado de la pregunta y luego inmediatamente la solución. No incluyas introducción alguna.
        No debes leer las alternativas, solo el enunciado y la solución.
        Para mencionar números, debes escribirlos en palabras. Por ejemplo, en lugar de "3640" debes escribir "tres mil seiscientos cuarenta".
        Para mencionar símbolos, debes escribirlos en palabras. Por ejemplo, en lugar de "%" debes escribir "por ciento".

        Responde únicamente con el texto del guión, sin ningún comentario o explicación.
        """

    def generate_script(self, solution: str, animation_code: str) -> str:
        response = self.client.chat_completion(
            system_prompt=self.system_prompt,
            user_prompt=f"Crea un guión para narrar y acompañar la siguiente solución paso a paso y código de animación:\n\nSolución: {solution}\n\nCódigo de animación: {animation_code}"
        )

        return response
