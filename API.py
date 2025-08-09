import requests

def obtener_departamentos():

    """Obtiene la lista completa de departamentos del Metropolitan Museum of Art desde su API.
    
    Realiza una petición GET al endpoint de departamentos de la API pública del Met y retorna
    los datos en formato JSON

    Returns:
        dict: Un diccionario con la respuesta JSON de la API que contiene:
            - 'departments' (list): Lista de diccionarios con información de departamentos
            - 'total' (int): Número total de departamentos disponibles

        Cada departamento en la lista contiene:
            - 'departmentId' (int): ID único del departamento
            - 'displayName' (str): Nombre público del departamento
    """

    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    return(response.json())
    

