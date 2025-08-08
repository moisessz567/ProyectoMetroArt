import requests

response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
datos = response.json()

print(datos)
# for obra in datos["objects"][:5]:

#     print(obra["objectID"], obra["department"])

