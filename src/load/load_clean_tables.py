import os
import psycopg2
from dotenv import load_dotenv

from src.transform.transform_pokemon import transform_pokemon
from src.utils.logger import logger

# Load environment variables
load_dotenv()

# Database connection
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()


# =========================
# LOAD FUNCTIONS
# =========================

def load_dim_pokemon(cursor, pokemon):

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


def load_dim_type(cursor, type_record):

    cursor.execute("""
        INSERT INTO dim_type (
            type_id,
            name
        )
        VALUES (%s, %s)

        ON CONFLICT (type_id) DO UPDATE SET
            name = EXCLUDED.name;
    """, (
        type_record["type_id"],
        type_record["name"]
    ))


def load_dim_ability(cursor, ability_record):

    cursor.execute("""
        INSERT INTO dim_ability (
            ability_id,
            name
        )
        VALUES (%s, %s)

        ON CONFLICT (ability_id) DO UPDATE SET
            name = EXCLUDED.name;
    """, (
        ability_record["ability_id"],
        ability_record["name"]
    ))


def load_fact_pokemon_type(cursor, type_link):

    cursor.execute("""
        INSERT INTO fact_pokemon_type (
            pokemon_id,
            type_id,
            slot
        )
        VALUES (%s, %s, %s)

        ON CONFLICT (pokemon_id, type_id) DO UPDATE SET
            slot = EXCLUDED.slot;
    """, (
        type_link["pokemon_id"],
        type_link["type_id"],
        type_link["slot"]
    ))


def load_fact_pokemon_ability(cursor, ability_link):

    cursor.execute("""
        INSERT INTO fact_pokemon_ability (
            pokemon_id,
            ability_id,
            is_hidden,
            slot
        )
        VALUES (%s, %s, %s, %s)

        ON CONFLICT (pokemon_id, ability_id) DO UPDATE SET
            is_hidden = EXCLUDED.is_hidden,
            slot = EXCLUDED.slot;
    """, (
        ability_link["pokemon_id"],
        ability_link["ability_id"],
        ability_link["is_hidden"],
        ability_link["slot"]
    ))


# =========================
# GET RAW DATA
# =========================

cursor.execute("""
    SELECT response_json
    FROM raw_api_responses
    WHERE endpoint = 'pokemon'
    ORDER BY resource_id;
""")

rows = cursor.fetchall()


# =========================
# MAIN LOOP
# =========================

for row in rows:

    try:

        data = row[0]

        transformed = transform_pokemon(data)

        pokemon = transformed["dim_pokemon"]

        logger.info(f"Loading Pokemon ID {pokemon['pokemon_id']}")

        load_dim_pokemon(cursor, pokemon)

        for type_record in transformed["dim_type"]:
            load_dim_type(cursor, type_record)

        for ability_record in transformed["dim_ability"]:
            load_dim_ability(cursor, ability_record)

        for type_link in transformed["fact_pokemon_type"]:
            load_fact_pokemon_type(cursor, type_link)

        for ability_link in transformed["fact_pokemon_ability"]:
            load_fact_pokemon_ability(cursor, ability_link)

    except Exception as e:

        logger.error(f"Failed processing Pokemon: {e}")

# =========================
# SAVE + CLOSE
# =========================

conn.commit()

cursor.close()

conn.close()

logger.info("Clean tables loaded successfully.")