import openai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def convertir_tiempo(segundos):
    """Convierte segundos a formato MM:SS."""
    minutos = int(segundos // 60)
    segundos = int(segundos % 60)
    return f"{minutos:02}:{segundos:02}"

def obtener_transcripcion(video_id):
    try:
        # Intenta obtener la transcripción en español
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    except NoTranscriptFound:
        print("Transcripción en español no disponible, intentando con el idioma predeterminado.")
        try:
            # Si no encuentra en español, intenta en el idioma por defecto
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except TranscriptsDisabled:
            print("El video no tiene transcripciones habilitadas.")
            return None
    except TranscriptsDisabled:
        print("El video no tiene transcripciones habilitadas.")
        return None
    except Exception as e:
        print(f"Error al obtener la transcripción: {e}")
        return None

    # Convertir la transcripción con marcas de tiempo en formato MM:SS
    return "\n".join(
        [f"{convertir_tiempo(entry['start'])}: {entry['text']}" for entry in transcript]
    )

def generar_metadata_youtube(transcripcion):
    if not transcripcion:
        return "No se pudo generar metadata ya que no hay transcripción disponible."
    
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
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente que ayuda a crear contenido para YouTube."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

def main(video_url):
    video_id = video_url.split("v=")[1]
    transcripcion = obtener_transcripcion(video_id)
    if transcripcion:
        metadata = generar_metadata_youtube(transcripcion)
        print("Resultado generado para YouTube:")
        print(metadata)
    else:
        print("No se pudo obtener la transcripción.")

# Llama a la función main con la URL de YouTube
main("https://www.youtube.com/watch?v=jh1GuEHyANs")
