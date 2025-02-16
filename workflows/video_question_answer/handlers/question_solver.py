from services.openai_service import OpenAIService
from services.deepseek_service import DeepSeekService

class QuestionSolver:
    def __init__(self):
        self.client = DeepSeekService()
        self.system_prompt = """
        Eres un experto en matemáticas. 
        Tu objetivo es resolver la pregunta paso a paso. 
        No debes saltarte ningún paso, y explicar cada paso como si la persona no sabe nada.
        Tu solución debe ser intuitiva y fácil de entender.
        Si utilizas fórmulas o propiedades, debes mostrarlas matemáticamente y explícitamente, no solo nombrarlas.
        Debes mostrar también el paso a paso de los cálculos, como multiplicaciones, divisiones, sumas, restas, etc.
        Tu formato de respuesta debe ser el siguiente:

        Enunciado:
        <enunciado>

        Solución paso a paso:
        <solución>

        Importante: Si el enunciado incluye tablas o gráficos, debes incluirlos en la sección de <enunciado>, en formato Markdown.
        Importante: Debes incluir todo el enunciado, incluyendo las tablas y gráficos.
        """

    def solve(self, question: str):
        response = self.client.chat_completion(
            system_prompt=self.system_prompt,
            user_prompt=question
        )
        return response
