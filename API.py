import requests
import json

def api():
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/[objectID]/name=Kiyohara Yukinobu")
    data = response.json()

    print(json.dumps(data, indent=4))

api()