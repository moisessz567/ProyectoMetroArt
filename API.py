import requests
import json

def obtener_departamentos():
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    return(response.json())
    
def obtener_obras():
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
    return(response.json())

def obtener_nacionalidades():
    response = requests.get()