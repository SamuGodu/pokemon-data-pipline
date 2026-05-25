-- Pokemon count by type
SELECT t.name, COUNT(*)
FROM dim_pokemon p
JOIN fact_pokemon_type ft
ON ft.pokemon_id = p.pokemon_id
    JOIN dim_type t
    ON ft.type_id = t.type_id
GROUP BY t.name