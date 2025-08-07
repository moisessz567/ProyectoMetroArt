import requests

response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
datos = response.json()

for departamento in datos["departments"][:10]:
    print(departamento["displayName"], departamento["departmentId"])

