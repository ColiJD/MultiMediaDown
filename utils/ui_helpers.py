from utils.url_cleaner import clean_url
from utils.downloader import download_video
from utils.excel_processor import process_excel

def download_single_video(link, download_type, st):
    """
    Descarga un solo video o audio a partir de un enlace proporcionado.
    
    :param link: URL del video de YouTube.
    :param download_type: Tipo de descarga ('video' o 'audio').
    :param st: Objeto de Streamlit para mostrar la interfaz de usuario.
    """
    if link:
        clean_link = clean_url(link)
        st.write(f"URL limpia: {clean_link}")
        
        # Crear una barra de progreso
        progress_bar = st.progress(0)
        try:
            result = download_video(clean_link, progress_bar, download_type)
            st.success(result)
        except Exception as e:
            st.error(str(e))
    else:
        st.warning("Por favor, ingrese un link válido.")

def download_multiple_videos_from_excel(uploaded_file, download_type, st):
    """
    Descarga múltiples videos o audios a partir de un archivo de Excel.
    
    :param uploaded_file: Archivo de Excel cargado por el usuario.
    :param download_type: Tipo de descarga ('video' o 'audio').
    :param st: Objeto de Streamlit para mostrar la interfaz de usuario.
    """
    if uploaded_file is not None:
        try:
            # Procesar el archivo de Excel
            links = process_excel(uploaded_file)
            
            if links:
                st.write(f"Se encontraron {len(links)} enlaces en el archivo:")
                for link in links:
                    st.write(link)
                
                if st.button("Descargar todos"):
                    for link in links:
                        clean_link = clean_url(link)
                        st.write(f"Descargando: {clean_link}")
                        
                        # Crear una barra de progreso para cada video/audio
                        progress_bar = st.progress(0)
                        try:
                            result = download_video(clean_link, progress_bar, download_type)
                            st.success(result)
                        except Exception as e:
                            st.error(str(e))
            else:
                st.warning("No se encontraron enlaces válidos en el archivo.")
        except Exception as e:
            st.error(str(e))