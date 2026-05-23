import json
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

raw_folder = "data/raw"

for filename in os.listdir(raw_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(raw_folder, filename)

        with open(file_path, "r") as file:
            data = json.load(file)

        pokemon_id = data["id"]
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

        cursor.execute(
            """
            INSERT INTO raw_api_responses (
                endpoint,
                resource_id,
                url,
                response_json,
                status_code
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (endpoint, resource_id) DO NOTHING;
            """,
            (
                "pokemon",
                pokemon_id,
                url,
                json.dumps(data),
                200
            )
        )

        print(f"Inserted raw response for Pokemon {pokemon_id}")

conn.commit()
cursor.close()
conn.close()

print("Raw JSON load complete.")