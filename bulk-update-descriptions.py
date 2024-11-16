from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define los alcances que necesita tu aplicación
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def generate_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)  # Reemplaza con el nombre correcto de tus credenciales
    creds = flow.run_local_server(port=0)
    
    # Guarda las credenciales en un archivo
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())
    print("Token generado y guardado en token.json.")


def update_video_descriptions(old_email, new_email):
    # Configurar credenciales (necesitarás obtenerlas previamente)
    creds = Credentials.from_authorized_user_file('token.json', 
        ['https://www.googleapis.com/auth/youtube.force-ssl'])
    
    # Crear servicio de YouTube
    youtube = build('youtube', 'v3', credentials=creds)
    
    # Obtener todos los videos del canal
    request = youtube.search().list(
        part='id,snippet',
        forMine=True,
        type='video',
        maxResults=50  # Ajusta según la cantidad de videos
    )
    response = request.execute()
    
    # Iterar sobre los videos
    for item in response['items']:
        video_id = item['id']['videoId']
        
        print(video_id)

        # Obtener detalles del video
        video_request = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        video_response = video_request.execute()
        
        # Obtener descripción actual
        description = video_response['items'][0]['snippet']['description']
        
        # Reemplazar correo electrónico
        new_description = description.replace(old_email, new_email)
        
        # Actualizar descripción si ha cambiado
        if new_description != description:
            # youtube.videos().update(
            #     part='snippet',
            #     body={
            #         'id': video_id,
            #         'snippet': {
            #             'categoryId': video_response['items'][0]['snippet']['categoryId'],
            #             'description': new_description
            #         }
            #     }
            # ).execute()
            print(f"Actualizado video: {video_id}")

# Uso:
generate_token()
update_video_descriptions('correo_viejo@ejemplo.com', 'correo_nuevo@ejemplo.com')