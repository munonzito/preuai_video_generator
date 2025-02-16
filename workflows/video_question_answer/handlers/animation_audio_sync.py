from services.openai_service import OpenAIService
from services.deepseek_service import DeepSeekService
from services.whisper_service import WhisperService

class AnimationAudioSync:
    def __init__(self):
        self.client = OpenAIService()
        self.whisper_client = WhisperService()
        self.system_prompt = """
        Eres un experto en ajustar los tiempos de animaciones en Python con Manim para que coincidan con el guión.
        Recibirás un guión con timestamps (los segundos en los que se dice cada parte del guión) y un código de animación.
        Tu objetivo es ajustar los tiempos self.wait() de cada animación para que coincidan exactamente con el guión.
        No modifiques el código de la animación, solo agrega o modificalos tiempos self.wait().
        El guión está en formato: (tiempo_inicio - tiempo_fin) texto_del_guión
        Puede que distintos chunks del guión se refieran a la misma animación. No asumas que distintos (tiempo_inicio - tiempo_fin) se refieren a distintas animaciones.
        Debes responder únicamente con el código de la animación con el tiempo ajustado, sin ningún comentario o explicación.
        """
    
    def _group_chunks(self, chunks: list, animation_code: str) -> list:
        """
        Agrupa los chunks que se refieren a la misma animación
        """
        
        system_prompt = """
        Eres un experto en agrupar chunks de un guión que se refieren a la misma animación.
        Recibirás un guión con timestamps y texto.
        Debes agrupar los chunks que se refieren a la misma animación y devolver el guión con el tiempo de inicio y fin de cada chunk.
        Responde únicamente con el guión con los tiempos ajustados, sin ningún comentario o explicación.
        """
        
        user_prompt = f"""
        Agrupa los chunks que se refieren a la misma "diapositiva".
        Las diapositivas suelen están separadas por FadeOut()
        Por ejemplo si el guión dice:

        '(0 - 5.16) Tenemos un grupo de datos, 12, 6, 14, 12 y 16.', '(5.88 - 9.08) Debemos determinar cuál de las siguientes afirmaciones es verdadera.', '(9.78 - 12.66) Primero, vamos a analizar las opciones una por una.'

        Y parte de la animación es:

        enunciado = Tex(
            "Tenemos un grupo de datos: 12, 6, 14, 12 y 16. Debemos determinar cuál de las siguientes afirmaciones es verdadera:", 
            font_size=30
        ).scale(0.7).to_edge(UP)
        alternativas = VGroup(
            Tex("A) El rango del grupo de datos es 4.", font_size=30).scale(0.7).next_to(enunciado, DOWN, buff=0.5),
            Tex("B) El promedio de los datos es 12.", font_size=30).scale(0.7).next_to(enunciado, DOWN, buff=1.2),
            Tex("C) La mediana de los datos es 14.", font_size=30).scale(0.7).next_to(enunciado, DOWN, buff=1.9),
            Tex("D) La moda de los datos es 16.", font_size=30).scale(0.7).next_to(enunciado, DOWN, buff=2.6),
        )
        
        self.play(Write(enunciado), Write(alternativas))

        FadeOut(enunciado)
        FadeOut(alternativas)

        Deberías devolver:

        (0 - 12.66) Tenemos un grupo de datos, 12, 6, 14, 12 y 16. Debemos determinar cuál de las siguientes afirmaciones es verdadera. Primero, vamos a analizar las opciones una por una.

        Y así con el resto del guión.

        Solo organiza el guión como se te indica.
        Solo debes modificarlo en caso de haber una palabra errónea. Pero el guión que debes devolver debe ser exactamente el mismo que el guión con timestamps.


        Guión con timestamps: {chunks}
        Código de animación: {animation_code}
        """

        response = self.client.chat_completion(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        return response
        
        

    def _transcribe_script(self, audio_file: str) -> str:
        """
        Transcribe un audio a texto y con timestamps
        """
        response = self.whisper_client.transcribe(audio_file)
        
        # # Formatear la respuesta
        # formatted_script = []
        # for chunk in response.get('chunks', []):
        #     if len(chunk.get('timestamp', [])) >= 2:
        #         t1 = chunk['timestamp'][0]
        #         t2 = chunk['timestamp'][1]
        #         formatted_script.append(f"({t1} - {t2}) {chunk['text'].strip()}")
        
        return response.get('chunks', [])

    def _remove_empty_awaits(self, animation_code: str) -> str:
        """
        Elimina los tiempos self.wait() que son cero.
        """
        animation_code = animation_code.replace("self.wait(0)", "")
        animation_code = animation_code.replace("self.wait(0.0)", "")
        animation_code = animation_code.replace(", run_time=0.0", "")
        return animation_code

    def synchronize(self, audio_file: str, animation_code: str) -> str:
        """
        Ajusta los tiempos de la animación para:
        1. Coincidir con la duración del audio
        2. Sincronizar con los eventos del guión
        3. Mantener ritmo narrativo
        """

        """
        1. Generar timestamps de cada evento del guión (Whisper)
        2. En base a las timestamps, ajustar los tiempos de las animaciones (OpenAI)
        3. Devolver el código de la animación con los tiempos ajustados (return)
        """

        # Generar timestamps de cada evento del guión (Whisper)
        whisper_response = self._transcribe_script(audio_file)
        print(whisper_response)

        animation_code = self._remove_empty_awaits(animation_code)

        # Agrupar chunks que se refieren a la misma animación
        # grouped_chunks = self._group_chunks(whisper_response, animation_code)
        # print(grouped_chunks)

        # En base a las timestamps, ajustar los tiempos de las animaciones (OpenAI)
        openai_response = self.client.chat_completion(
            system_prompt=self.system_prompt,
            user_prompt=f"""
            En base a los timestamps del guión, ajusta el código de la animación, agregando tiempos self.wait() y run_time para que las animaciones coincidan EXACTAMENTE con el guión.
            Cada "diapositiva" de la animación debe coincidir con la parte del guión respectiva.
            Guión con timestamps: {whisper_response}

            Código de animación:
            {animation_code}
            """,
            model="o1-mini"
        )

        print(openai_response)

        animation_code = self._remove_empty_awaits(openai_response)

        return animation_code
