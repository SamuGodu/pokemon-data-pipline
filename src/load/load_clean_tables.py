import os
import psycopg2
from dotenv import load_dotenv

from src.transform.transform_pokemon import transform_pokemon

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

cursor.execute("""
    SELECT response_json
    FROM raw_api_responses
    WHERE endpoint = 'pokemon'
    ORDER BY resource_id;
""")

rows = cursor.fetchall()

for row in rows:
    data = row[0]
    transformed = transform_pokemon(data)

    pokemon = transformed["dim_pokemon"]

    cursor.execute("""
        INSERT INTO dim_pokemon (
            pokemon_id,
            name,
            height,
            weight,
            base_experience,
            is_default
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (pokemon_id) DO UPDATE SET
            name = EXCLUDED.name,
            height = EXCLUDED.height,
            weight = EXCLUDED.weight,
            base_experience = EXCLUDED.base_experience,
            is_default = EXCLUDED.is_default;
    """, (
        pokemon["pokemon_id"],
        pokemon["name"],
        pokemon["height"],
        pokemon["weight"],
        pokemon["base_experience"],
        pokemon["is_default"]
    ))

conn.commit()
cursor.close()
conn.close()

print("dim_pokemon loaded successfully.")