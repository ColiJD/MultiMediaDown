import streamlit as st
from PIL import Image
import pandas as pd
import yt_dlp as ytdlp
import os
import requests

# Ruta a FFmpeg
ffmpeg_path = r"C:\ffmpeg\bin"


# Crea una sesión de requests para manejar las cookies de YouTube
session = requests.Session()

def save_cookies_to_netscape_format(cookies, filename):
    with open(filename, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# This is a generated file! Do not edit.\n")
        for cookie in cookies:
            # Línea en formato Netscape
            f.write(f"{cookie.domain}\t{'TRUE' if cookie.domain.startswith('.') else 'FALSE'}\t{cookie.path}\t{'TRUE' if cookie.secure else 'FALSE'}\t{cookie.expires}\t{cookie.name}\t{cookie.value}\n")

def download_audio(url):
    try:
        st.write(f'Leyendo URL: {url}')
        
        # Realiza una solicitud GET para obtener cookies y usar headers personalizados
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        response = session.get(url, headers=headers)
        if response.status_code != 200:
            st.error(f'Error al acceder a la URL: {response.status_code}')
            return
        
        # Guardar las cookies en formato Netscape
        save_cookies_to_netscape_format(session.cookies, 'cookies.txt')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path,  # Ruta a FFmpeg
            'cookiefile': 'cookies.txt',  # Archivo donde se almacenan las cookies
            'quiet': True,  # Suprime los logs de yt_dlp
        }
        
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Unknown Title')
            st.write(f'Título: {title}')
            st.write('Descarga completada.')

        st.write('-----------------------------------------')
    except Exception as e:
        st.error(f'Error al descargar el audio: {e}')

# Diseño de la aplicación

# Cargar la imagen del logo
try:
    logo = Image.open('assets/gordo.webp')
except FileNotFoundError:
    st.sidebar.error('No se encontró la imagen del logo en "assets/gordo.webp".')
    logo = None

with st.sidebar:
    if logo:
        st.image(logo, width=150)  # Ajusta el ancho de la imagen si es necesario
    file_path = st.file_uploader("Selecciona un archivo con URLs (Excel)")
    tipo = st.selectbox("Tipo de Descarga", ['-', 'audio'])
        
st.title('Descarga de YouTube')

if file_path:
    try:
        df = pd.read_excel(file_path)
        st.header("Archivo a Descargar")
        st.dataframe(df)
    except Exception as e:
        st.error(f'Error al leer el archivo: {e}')
        df = None
else:
    st.warning("Por favor, selecciona un archivo válido con URLs.")

if 'df' in locals() and df is not None:
    if tipo == 'audio':
        st.header("Estado de Descargas")
        with st.expander('Detalle de Descarga'):
            for idx, row in df.iterrows():
                url = row.get('url')
                if pd.isna(url):
                    st.error(f'La fila {idx} no contiene una URL válida.')
                    continue
                download_audio(url)
    elif tipo == '-':
        st.warning("Por favor, selecciona el tipo de descarga.")
else:
    st.info("Esperando a que se cargue un archivo con URLs.")
