from manim import *
import os
import subprocess

class AnimationGenerator:
    def __init__(self, output_dir: str = "animations_output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_animation(self, animation_file: str, scene_name: str = None):
        """
        Genera la animación usando Manim.
        
        Args:
            animation_file: Nombre del archivo que contiene el código de la animación
            scene_name: Nombre de la clase Scene a renderizar (opcional)
        """
        # Comando base para ejecutar la animación
        command = [
            "manim",
            "-pqm",  # Produce media calidad y previsualiza el resultado
            "--media_dir", self.output_dir,  # Directorio de salida
            animation_file,  # Archivo con el código de la animación
        ]

        # Si se especifica una escena específica, agregarla al comando
        if scene_name:
            command.append(scene_name)
        
        try:
            # Ejecutar el comando
            subprocess.run(command, check=True)
            print(f"\nAnimación generada exitosamente en el directorio: {self.output_dir}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"\nError al generar la animación: {e}")
            return False
        except Exception as e:
            print(f"\nError inesperado: {e}")
            return False 