import streamlit as st
from utils.ui_helpers import download_single_video, download_multiple_videos_from_excel

def main():
    """
    Función principal que maneja la interfaz de usuario y la lógica de la aplicación.
    """
    st.subheader("Descargador de Videos/Audios de YouTube")
    st.info("Por favor, sigue estos pasos para agregar el enlace del video:\n\n1. Abre el video que deseas descargar.\n2. Busca y haz clic en la opción **Compartir** (normalmente está debajo del video o en los botones de opciones).\n3. Selecciona la opción **Copiar enlace** o **Copiar URL**.\n4. Pega el enlace copiado en el cuadro correspondiente de nuestro programa.")


    # Opción para seleccionar el tipo de descarga
    download_type = st.radio("Seleccione el tipo de descarga:", ('video', 'audio'))
    st.info("Las descargas se quedan guardas en: C:\AYVdownload")

    # Opción para ingresar un enlace manualmente
    st.subheader("Descargar un video/audio")
    manual_link = st.text_input("Ingrese el link del video de YouTube: ",)

    if st.button("Descargar manualmente"):
        download_single_video(manual_link, download_type, st)

    # Opción para cargar un archivo de Excel con múltiples enlaces
    st.subheader("Descargar desde un archivo de Excel")
    st.info("Por favor, sigue estos pasos para agregar los link en el archivo :\n\n1. En la primera columna del archivo como titulo se pone link .\n2. En la misma columna debajo del titulo se van agregando los link a descargar**")
    uploaded_file = st.file_uploader("Cargue un archivo de Excel con enlaces de YouTube", type=["xlsx", "xls"])
    download_multiple_videos_from_excel(uploaded_file, download_type, st)

if __name__ == "__main__":
    main()