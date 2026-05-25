SELECT endpoint, resource_id, status_code, fetched_at
FROM raw_api_responses
ORDER BY resource_id;

SELECT COUNT(*)
FROM raw_api_responses;

SELECT *
FROM dim_pokemon
ORDER BY pokemon_id;

SELECT *
FROM fact_pokemon_ability

SELECT COUNT(*) FROM dim_pokemon;
SELECT COUNT(*) FROM dim_type;
SELECT COUNT(*) FROM dim_ability;
SELECT COUNT(*) FROM fact_pokemon_type;
SELECT COUNT(*) FROM fact_pokemon_ability;