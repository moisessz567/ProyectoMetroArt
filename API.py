import requests
import json

def __init__ (self):
    """INIT
    Recibe: n\a
    Retorna: n\
    """
    pass

def pull_departamentos():
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    return(response.json())
    
    # for departamento in datos["departments"][:10]:
    #     print(departamento["departmentId"], departamento["displayName"])


    


