import json
import requests

for pokemon_id in range(1,10):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    response = requests.get(url)

    if response.status_code == 200:
        print(response.status_code)
    else:
        print("Something failed")
        continue
    
    data = response.json()

    file_path = f"data/raw/pokemon_{pokemon_id}.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved Pokemon {pokemon_id}")
