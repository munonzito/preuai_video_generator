from workflows.video_question_answer.handlers import (
    QuestionSolver, AnimationCoder, VoiceGenerator, 
    ScriptGenerator, AnimationAudioSync, AnimationGenerator,
    VideoAudioMerger
)
from workflows.video_question_answer.pipeline import GenerateVideoPipeline
from services.whisper_service import WhisperService

# Inputs

# question = """Un hotel tiene 200 habitaciones y para un fin de semana largo tiene reservadas 140 habitaciones.
# ¿Cuál es el porcentaje de habitaciones que aún están disponibles ese fin de semana?
# A)30 %
# B)43 %
# C)60 %
# D)70 %"""

question = """
¿Cuál de las siguientes opciones representa al número (888)^2?

A) 2^6 * 111^2
B) 2^6 * 111
C) 2^5 * 111^2
D) 2^5 * 111
"""

pipeline = GenerateVideoPipeline()

pipeline.generate_video(question, "animations_output/q2")

#Transcribir audio
#whisper_service = WhisperService()
#whisper_response = whisper_service.transcribe("audio.mp3")
#print(whisper_response)


# # 1. Resolver pregunta paso a paso
# question_solver = QuestionSolver()
# solution = question_solver.solve(question)

# print(solution)

# # 2. Generar código de animación
# animation_coder = AnimationCoder()
# animation_code = animation_coder.code(solution)

# # print(animation_code)

# # 3. Generar guion en base a la solución y el código de animación
# # Inputs: solution, animation_code
# script_generator = ScriptGenerator()
# script = script_generator.generate_script(solution, animation_code)

# print(script)

# # 4. Ajustar tiempo de la animación para que coincida con el guion
# # Inputs: script, animation_code
# animation_audio_sync = AnimationAudioSync()
# animation_code = animation_audio_sync.synchronize(script, animation_code)

# # Escribir el código en un archivo
# with open("animation_code.py", "w") as f:
#     # Remover ```python y ```
#     f.write(animation_code.replace("```python", "").replace("```", ""))

# # 5. Generar voz
# # Inputs: script
# voice_generator = VoiceGenerator()
# voice_audio = voice_generator.generate_voice(script)
# #Guardar audio
# with open("audio.mp3", "wb") as f:
#     for audio_chunk in voice_audio:
#         f.write(audio_chunk)


# # 6. Generar video
# # Inputs: animation_code
# animation_generator = AnimationGenerator(output_dir="animations_output/q1")
# animation_generator.generate_animation("animation_code.py")

# # 7. Juntar audio y video
# video_audio_merger = VideoAudioMerger()

# # Obtener ruta del video generado
# video_dir = os.path.join("animations_output/q1/videos/animation_code/720p30")
# video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
# if video_files:
#     video_path = os.path.join(video_dir, video_files[0])
#     audio_path = "audio.mp3"
#     output_path = os.path.join("animations_output/q1", "video_final.mp4")
    
#     # Combinar video y audio
#     success = video_audio_merger.merge(video_path, audio_path, output_path)
    
#     if success:
#         print("Proceso completo. Video final generado con éxito.")
#     else:
#         print("Error al generar el video final.")
# else:
#     print("No se encontró el archivo de video generado.")

