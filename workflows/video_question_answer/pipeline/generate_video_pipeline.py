import os
from workflows.video_question_answer.handlers import (
    QuestionSolver, AnimationCoder, VoiceGenerator, ScriptGenerator, AnimationAudioSync, AnimationGenerator, VideoAudioMerger, AnimationFixerHandler
)

class GenerateVideoPipeline:
    def __init__(self):
        self.question_solver = QuestionSolver()
        self.animation_coder = AnimationCoder()
        self.script_generator = ScriptGenerator()
        self.animation_audio_sync = AnimationAudioSync()
        self.voice_generator = VoiceGenerator()
        self.animation_generator = AnimationGenerator()
        self.video_audio_merger = VideoAudioMerger()
        self.animation_fixer_handler = AnimationFixerHandler()
    def generate_video(self, question: str, output_dir: str) -> bool:
        # Paso 1: Resolver pregunta
        print("Resolviendo pregunta...")
        solution = self.question_solver.solve(question)

        print(solution)
            
        # Paso 2: Generar código de animación inicial
        print("Generando código de animación inicial...")
        animation_code = self.animation_coder.code(solution)
        
        # Paso 3: Generar guión
        print("Generando guión...")
        script = self.script_generator.generate_script(solution, animation_code)

        # Paso 4: Generar voz
        voice_audio = self.voice_generator.generate_voice(script)
        temp_audio_path = os.path.join(output_dir, "temp_audio.mp3")
        os.makedirs(os.path.dirname(temp_audio_path), exist_ok=True)
        with open(temp_audio_path, "wb") as f:
            for audio_chunk in voice_audio:
                f.write(audio_chunk)
        
        # Paso 5: Sincronizar animación con audio
        print("Sincronizando animación con audio...")
        animation_code = self.animation_audio_sync.synchronize(temp_audio_path, animation_code)

        # # Paso 6: Corregir código de animación
        # print("Corrigiendo código de animación...")
        # animation_code = self.animation_fixer_handler.fix_animation_code(animation_code)

        # Escribir código temporal
        print("Escribiendo código temporal...")
        temp_code_path = os.path.join(output_dir, "temp_animation.py")
        os.makedirs(os.path.dirname(temp_code_path), exist_ok=True)
        with open(temp_code_path, "w") as f:
            f.write(animation_code.replace("```python", "").replace("```", ""))
        
        # Paso 7: Generar animación
        self.animation_generator.output_dir = output_dir
        self.animation_generator.generate_animation(temp_code_path)
        
        # Paso 8: Combinar audio y video
        video_dir = os.path.join(output_dir, "videos/temp_animation/720p30")
        video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
        
        if not video_files:
            return False
            
        video_path = os.path.join(video_dir, video_files[0])
        final_output = os.path.join(output_dir, "video_final.mp4")
        
        return self.video_audio_merger.merge(
            video_path, 
            temp_audio_path, 
            final_output
        )