from services.openai_service import OpenAIService
from services.deepseek_service import DeepSeekService
class AnimationCoder:
    def __init__(self):
        self.client = DeepSeekService()
        self.system_prompt = """
        Eres un experto en crear animaciones matemáticas usando python y la librería de Manim.
        El usuario te proporcionará un guión explicando y narrando la solución paso a paso de una pregunta de matemáticas.
        Tu objetivo es crear una animación con python y Manim que muestre el proceso paso a paso de la solución de la pregunta.
        Responde únicamente con el código de la animación, sin ningún comentario o explicación.
        Inicialmente, debes mostrar el enunciado y contextualización del problema completo en la parte superior de la pantalla (usando el objeto Tex(), con una letra con scale(0.7)) y no debes omitir ningún dato importante necesario para resolver el problema. Debajo de este debes ubicar las alternativas, ordenadas verticalmente.
        Luego, debes borrar el enunciado y las alternativas, y comenzar con el paso a paso para resolver el problema.
        Evita que los pasos se solapen o superpongan.
        Una vez finalizado el paso a paso, LIMPIA COMPLETAMENTE la pantalla (IMPORTANTE).
        Luego, vuelve a mostrar el enunciado y las alternativas, y encierra en un rectángulo la alternativa correcta.

 
        Importante: Debes limpiar la pantalla con FadeOut() para que no se escriban los textos unos encima de otros.
        Importante: Las alternativas deben verse ordenadas.
        Importante: Si tienes que mostrar tablas en el enunciado. Primero muestra el enunciado, luego muestra las tablas. Limpia la pantalla, muestra el enunciado y las alternativas. Es decir, no muestres las tablas y alternativas en el mismo frame, ya que no hay espacio para ello.
        Importante: Si el enunciado incluye tablas o gráficos, debes incluirlos. 
        Importante: Debes incluir todo el enunciado, incluyendo las tablas y gráficos.
        Importante: Evita mostrar muchos textos en el mismo frame, ya que puede que se salgan de la pantalla. Cada paso debe mostrarse en frame distintos.

        REGLAS CRÍTICAS DE FORMATO:
        1. Para texto normal usar Tex(), y si tienen matemáticas, usar Tex pero con $expresion$, donde expresión es la expresión matemática. Por ejemplo Tex("Hola $x^2$"). Si necesitas utilizar \\ (backslash) dentro del Tex, debes escribirlo dentro de un $$, porque si no se obtiene error de compilación por missing $.
        2. Para ecuaciones completas, usa MathTex(). Por ejemplo MathTex("x^2 + y^2 = z^2").
        3. No uses doble slash dentro del Tex, ya que eso causará un error. Escribe el Tex normalmente, y si necesitas matemáticas, usa $expresion$ dentro del Tex.
        4. No uses saltos de línea. Prefiere usar otro objeto Tex o poner todo el texto en un solo objeto Tex.
        5. Los textos deben ser legibles para pantallas de celular
                             """

    def code(self, solution: str):
        response = self.client.chat_completion(
            system_prompt=self.system_prompt,
            user_prompt=solution,
            model="o1-mini"
        )

        return response