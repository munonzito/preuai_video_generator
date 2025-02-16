# Ejecutar la animación de animation_code.py

from manim import *
import os
import subprocess

def generate_animation():
    # Configurar la calidad y el directorio de salida
    output_dir = "animations_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Comando para ejecutar la animación
    command = [
        "manim",
        "-pqm",  # Produce media calidad y previsualiza el resultado
        "--media_dir", output_dir,  # Directorio de salida
        "animation_code.py",  # Archivo con el código de la animación
    ]
    
    try:
        # Ejecutar el comando
        subprocess.run(command, check=True)
        print(f"\nAnimación generada exitosamente en el directorio: {output_dir}")
        
    except subprocess.CalledProcessError as e:
        print(f"\nError al generar la animación: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    generate_animation()


