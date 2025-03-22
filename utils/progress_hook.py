import re

def progress_hook(d, progress_bar):
    """
    Hook para actualizar la barra de progreso.
    
    :param d: Diccionario con la información de progreso.
    :param progress_bar: Objeto de barra de progreso de Streamlit.
    """
    if d['status'] == 'downloading':
        # Eliminar caracteres de escape ANSI usando una expresión regular
        percent_str = re.sub(r'\x1b\[[0-9;]*m', '', d['_percent_str'])
        progress = float(percent_str.strip('%')) / 100  # Convertir porcentaje a valor entre 0 y 1
        progress_bar.progress(progress)
    elif d['status'] == 'finished':
        progress_bar.progress(1.0)  # Completar la barra al 100%