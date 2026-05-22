import json
import requests

for pokemon_id in range(1,10):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    response = requests.get(url)

    print(response.status_code)

    data = response.json()

    file_path = f"data/raw/pokemon_{pokemon_id}"

    with open("data/raw/pokemon_1.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved Pokemon {pokemon_id}")