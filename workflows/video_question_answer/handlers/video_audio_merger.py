from moviepy import VideoFileClip, AudioFileClip
import os

class VideoAudioMerger:
    def __init__(self):
        pass

    def merge(self, video_path: str, audio_path: str, output_path: str) -> bool:
        """
        Combina un video con un archivo de audio.
        
        Args:
            video_path: Ruta al archivo de video
            audio_path: Ruta al archivo de audio
            output_path: Ruta donde se guardará el video final
            
        Returns:
            bool: True si la operación fue exitosa, False si hubo error
        """
        try:
            # Crear el directorio de salida si no existe
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Cargar video y audio
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            # Combinar video con audio
            final_clip = video_clip.with_audio(audio_clip)

            # Guardar el video final
            final_clip.write_videofile(output_path)

            # Cerrar los clips para liberar memoria
            video_clip.close()
            audio_clip.close()
            final_clip.close()

            print(f"\nVideo con audio generado exitosamente en: {output_path}")
            return True

        except Exception as e:
            print(f"\nError al combinar video y audio: {e}")
            return False 