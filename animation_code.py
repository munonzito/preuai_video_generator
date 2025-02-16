
from manim import *

class HotelRoomsPercentage(Scene):
    def construct(self):
        # Mostrar enunciado y opciones
        enunciado = Tex(
            "Un hotel tiene 200 habitaciones y para un fin de semana largo tiene reservadas 140 habitaciones. "
            "Se pregunta cuál es el porcentaje de habitaciones que aún están disponibles ese fin de semana."
        ).scale(0.7).to_edge(UP)
        opciones = VGroup(
            Tex("A) 30 \\%").scale(0.7),
            Tex("B) 43 \\%").scale(0.7),
            Tex("C) 60 \\%").scale(0.7),
            Tex("D) 70 \\%").scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(enunciado, DOWN, buff=0.5)

        self.play(Write(enunciado), Write(opciones))
        self.wait(8)

        # Borrar enunciado y opciones
        self.play(FadeOut(enunciado), FadeOut(opciones))

        # Paso 1: Habitaciones disponibles
        step1 = MathTex(
            "200 - 140 = 60"
        ).scale(1.2)
        self.play(Write(step1))
        self.wait(6)

        # Borrar paso 1
        self.play(FadeOut(step1))

        # Paso 2: Fórmula para porcentaje
        step2 = MathTex(
            "\\text{Porcentaje disponible} = \\left( \\frac{60}{200} \\right) \\times 100"
        ).scale(1.2)
        self.play(Write(step2))
        self.wait(8)

        # Borrar paso 2
        self.play(FadeOut(step2))

        # Paso 3: División
        step3 = MathTex(
            "\\frac{60}{200} = 0.3"
        ).scale(1.2)
        self.play(Write(step3))
        self.wait(6)

        # Borrar paso 3
        self.play(FadeOut(step3))

        # Paso 4: Multiplicación
        step4 = MathTex(
            "0.3 \\times 100 = 30"
        ).scale(1.2)
        self.play(Write(step4))
        self.wait(6)

        # Borrar paso 4
        self.play(FadeOut(step4))

        # Mostrar enunciado y opciones nuevamente, con respuesta correcta resaltada
        enunciado_final = Tex(
            "Un hotel tiene 200 habitaciones y para un fin de semana largo tiene reservadas 140 habitaciones. "
            "Se pregunta cuál es el porcentaje de habitaciones que aún están disponibles ese fin de semana."
        ).scale(0.7).to_edge(UP)
        opciones_final = VGroup(
            Tex("A) 30 \\%").scale(0.7),
            Tex("B) 43 \\%").scale(0.7),
            Tex("C) 60 \\%").scale(0.7),
            Tex("D) 70 \\%").scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(enunciado_final, DOWN, buff=0.5)

        self.play(Write(enunciado_final), Write(opciones_final))
        self.wait(8)

        # Resaltar opción correcta
        rectangulo = SurroundingRectangle(opciones_final[0], color=GREEN, buff=0.2)
        self.play(Create(rectangulo))
        self.wait(6)
