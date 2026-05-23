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

print(pokemon_id)
print(name)
print(height)
print(weight)
print(base_experience)
print(is_default)
