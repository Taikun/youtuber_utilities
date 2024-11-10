import openai
import whisper
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def convertir_tiempo(segundos):
    """Convierte segundos a formato MM:SS."""
    minutos = int(segundos // 60)
    segundos = int(segundos % 60)
    return f"{minutos:02}:{segundos:02}"

def transcribir_video(video_path):
    # Carga el modelo Whisper para transcribir
    modelo = whisper.load_model("base")  # Usa 'small', 'medium', o 'large' para mayor precisión
    resultado = modelo.transcribe(video_path)
    
    # Convierte la transcripción con marcas de tiempo en formato MM:SS
    transcripcion = "\n".join(
        [f"{convertir_tiempo(segment['start'])}: {segment['text']}" for segment in resultado['segments']]
    )
    return transcripcion

def generar_metadata_youtube(transcripcion):
    # Crear un prompt detallado para generar título, descripción, etiquetas y capítulos
    prompt = f"""
    A partir de la siguiente transcripción, genera un título atractivo, una descripción detallada, etiquetas separadas por comas y una lista de capítulos con sus marcas de tiempo en formato MM:SS.

    Transcripción:
    {transcripcion}

    Quiero el resultado en el siguiente formato:

    Título:
    [Título generado]

    Descripción:
    [Descripción generada]

    Etiquetas:
    [etiqueta1, etiqueta2, etiqueta3, ...]

    Capítulos:
    [00:00 Introducción]
    [03:45 Tema principal]
    [07:30 Conclusión]
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un asistente que ayuda a crear contenido para YouTube."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

def main(video_path):
    transcripcion = transcribir_video(video_path)
    if transcripcion:
        metadata = generar_metadata_youtube(transcripcion)
        print("Resultado generado para YouTube:")
        print(metadata)
    else:
        print("No se pudo obtener la transcripción.")

# Llama a la función main con la ruta del archivo de video
main("/mnt/f/YoutubeVideos/ActualizaciónGATrueNAS.mp4")
