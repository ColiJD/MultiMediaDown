import pandas as pd

def process_excel(file):
    """
    Procesa un archivo de Excel para extraer los enlaces de YouTube.
    
    :param file: Archivo de Excel cargado por el usuario.
    :return: Lista de enlaces de YouTube.
    """
    try:
        # Leer el archivo de Excel
        df = pd.read_excel(file)
        
        # Suponemos que los enlaces están en la primera columna
        links = df.iloc[:, 0].dropna().tolist()  # Extraer la primera columna y eliminar valores nulos
        return links
    except Exception as e:
        raise Exception(f'Error al procesar el archivo de Excel: {str(e)}')