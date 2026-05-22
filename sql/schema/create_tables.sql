-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS fact_pokemon_ability;
DROP TABLE IF EXISTS fact_pokemon_type;
DROP TABLE IF EXISTS dim_ability;
DROP TABLE IF EXISTS dim_type;
DROP TABLE IF EXISTS dim_pokemon;
DROP TABLE IF EXISTS raw_api_responses;


-- Raw API response storage
CREATE TABLE raw_api_responses (
    id SERIAL PRIMARY KEY,
    endpoint VARCHAR(100) NOT NULL,
    resource_id INTEGER,
    url TEXT NOT NULL,
    response_json JSONB NOT NULL,
    status_code INTEGER NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT unique_raw_response UNIQUE (endpoint, resource_id)
);

-- Main Pokemon dimension table
CREATE TABLE dim_pokemon (
    pokemon_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER,
    is_default BOOLEAN,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pokemon type dimension table
CREATE TABLE dim_type (
    type_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Pokemon abiklity dimension table
CREATE TABLE dim_ability (
    ability_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Many-to-many relationship between Pokemon and Types
CREATE TABLE fact_pokemon_type (
    pokemon_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    slot INTEGER,

PRIMARY KEY (pokemon_id, type_id),

CONSTRAINT fk_pokemon_type_pokemon
    FOREIGN KEY (pokemon_id)
    REFERENCES dim_pokemon (pokemon_id),
    
CONSTRAINT fk_pokemon_type_type
    FOREIGN KEY (type_id)
    REFERENCES dim_type (type_id)
);

-- Many-to-many relationship between Pokemon and Ability
CREATE TABLE fact_pokemon_ability (
    pokemon_id INTEGER NOT NULL,
    ability_id INTEGER NOT NULL,
    is_hidden BOOLEAN,
    slot INTEGER,

PRIMARY KEY (pokemon_id, ability_id),

CONSTRAINT fk_pokemon_ability_pokemon
    FOREIGN KEY (pokemon_id)
    REFERENCES dim_pokemon (pokemon_id),
    
CONSTRAINT fk_pokemon_ability_ability
    FOREIGN KEY (ability_id)
    REFERENCES dim_ability (ability_id)
);


-- Indexes for faster joins and filtering
CREATE INDEX idx_raw_api_endpoint
ON raw_api_responses(endpoint);

CREATE INDEX idx_pokemon_name
ON dim_pokemon(name);

CREATE INDEX idx_fact_pokemon_type_type_id
ON fact_pokemon_type(type_id);

CREATE INDEX idx_fact_pokemon_ability_ability_id
ON fact_pokemon_ability(ability_id);