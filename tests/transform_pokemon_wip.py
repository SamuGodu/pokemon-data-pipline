import json

file_path = "data/raw/pokemon_1.json"

with open(file_path, "r") as file:
    data = json.load(file)


# dim_pokemon
pokemon_id = data['id']
name = data['name']
height = data['height']
weight = data['weight']
base_experience = data['base_experience']
is_default = data['is_default']

dim_pokemon_row = {
    "pokemon_id": pokemon_id,
    "name": name,
    "height": height,
    "weight": weight,
    "base_experience": base_experience,
    "is_default": is_default
}

abilities = []

for item in data["abilities"]:

    slot = item["slot"]
    ability_name = item["ability"]["name"]
    ability_url = item['ability']['url']
    ability_id = int(ability_url.split('/')[-2])
    is_hidden = item["is_hidden"]

    abilities.append ({
        'ability_id': ability_id,
        'ability_name': ability_name,
        'slot': slot,
        'is_hidden': is_hidden
    })

# dim_ability
dim_ability_rows = []

for ability in abilities:
    dim_ability_rows.append({
        "ability_id": ability["ability_id"],
        "name": ability["ability_name"]
    })

types = []

for item in data["types"]:

    slot = item["slot"]
    type_name = item["type"]["name"]
    type_url = item['type']['url']
    type_id = int(type_url.split('/')[-2])

    types.append ({
        'type_id': type_id,
        'type_name': type_name,
        'slot': slot
    })


# dim_types
dim_type_rows = []

for type_record in types:
    dim_type_rows.append({
        "type_id": type_record["type_id"],
        "name": type_record["type_name"]
    })


#fact_pokemon_type
fact_pokemon_type_rows = []

for type_record in types:
    fact_pokemon_type_rows.append({
        "pokemon_id": pokemon_id,
        "type_id": type_record["type_id"],
        "slot": type_record["slot"]
    })


#fact_pokemon_abilities
fact_pokemon_ability_rows = []

for ability in abilities:
    fact_pokemon_ability_rows.append({
        "pokemon_id": pokemon_id,
        "ability_id": ability["ability_id"],
        "is_hidden": ability["is_hidden"],
        "slot": ability["slot"]
    })


print("dim_ability:", dim_ability_rows)
print("fact_pokemon_ability:", fact_pokemon_ability_rows)
print("dim_type:", dim_type_rows)
print("fact_pokemon_type:", fact_pokemon_type_rows)
print("dim_pokemon:", dim_pokemon_row)