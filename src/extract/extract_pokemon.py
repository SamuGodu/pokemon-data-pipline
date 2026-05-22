import json
import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data["name"])

with open("data/raw/pokemon_1.json", "w") as file:
    json.dump(data, file, indent=4)

print("Raw JSON saved.")