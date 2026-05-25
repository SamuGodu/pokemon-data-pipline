import json

def get_id_from_url(url):
    return int(url.rstrip("/").split("/")[-1])

def transform_pokemon(data):
    pokemon_id = data["id"]

    dim_pokemon_row = {
        "pokemon_id": pokemon_id,
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"],
        "is_default": data["is_default"]
    }

    dim_ability_rows = []
    fact_pokemon_ability_rows = []

    for item in data["abilities"]:
        ability_url = item["ability"]["url"]
        ability_id = int(ability_url.split("/")[-2])

        dim_ability_rows.append({
            "ability_id": ability_id,
            "name": item["ability"]["name"]
        })

        fact_pokemon_ability_rows.append({
            "pokemon_id": pokemon_id,
            "ability_id": ability_id,
            "is_hidden": item["is_hidden"],
            "slot": item["slot"]
        })

    dim_type_rows = []
    fact_pokemon_type_rows = []

    for item in data["types"]:
        type_url = item["type"]["url"]
        type_id = int(type_url.split("/")[-2])

        dim_type_rows.append({
            "type_id": type_id,
            "name": item["type"]["name"]
        })

        fact_pokemon_type_rows.append({
            "pokemon_id": pokemon_id,
            "type_id": type_id,
            "slot": item["slot"]
        })

    return {
        "dim_pokemon": dim_pokemon_row,
        "dim_ability": dim_ability_rows,
        "fact_pokemon_ability": fact_pokemon_ability_rows,
        "dim_type": dim_type_rows,
        "fact_pokemon_type": fact_pokemon_type_rows
    }
