import yt_dlp
from .progress_hook import progress_hook
import os

# Definir la ruta base y las subcarpetas
DOWNLOAD_FOLDER = r"C:\AYVdownload"  # Ruta absoluta en Windows
VIDEOS_FOLDER = os.path.join(DOWNLOAD_FOLDER, "videos")  # Subcarpeta para videos
AUDIOS_FOLDER = os.path.join(DOWNLOAD_FOLDER, "audios")  # Subcarpeta para audios
def download_video(link, progress_bar, download_type):
    """
    Descarga un video o solo el audio de YouTube usando yt-dlp.
    
    :param link: URL del video de YouTube.
    :param progress_bar: Objeto de barra de progreso de Streamlit.
    :param download_type: Tipo de descarga ('video' o 'audio').
    """
    if download_type == 'video':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Descargar el mejor video y audio
            'outtmpl': os.path.join(VIDEOS_FOLDER, '%(title)s.%(ext)s'),  # Guardar en la carpeta de videos
            'progress_hooks': [lambda d: progress_hook(d, progress_bar)],  # Hook de progreso
        }
    elif download_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',  # Descargar solo el mejor audio
            'outtmpl': os.path.join(AUDIOS_FOLDER, '%(title)s.%(ext)s'),  # Guardar en la carpeta de audios
            'extractaudio': True,  # Extraer solo el audio
            'audioformat': 'mp3',  # Formato de salida del audio
            'progress_hooks': [lambda d: progress_hook(d, progress_bar)],  # Hook de progreso
        }
    else:
        raise ValueError("Tipo de descarga no válido.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return f'{"Video" if download_type == "video" else "Audio"} descargado correctamente: {link}, '
    except Exception as e:
        raise Exception(f'Error durante la descarga de {link}: {str(e)}')