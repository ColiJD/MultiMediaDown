import urllib.parse

def clean_url(link):
    """
    Limpia la URL eliminando los parámetros de consulta.
    
    :param link: URL a limpiar.
    :return: URL limpia sin parámetros de consulta.
    """
    parsed_url = urllib.parse.urlparse(link)
    clean_url = parsed_url._replace(query='').geturl()  # Elimina los parámetros de consulta
    return clean_url