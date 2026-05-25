-- Pokemon count by type
SELECT t.name, COUNT(*)
FROM dim_pokemon p
JOIN fact_pokemon_type ft
ON ft.pokemon_id = p.pokemon_id
    JOIN dim_type t
    ON ft.type_id = t.type_id
GROUP BY t.name

-- Average hieght and weight by type
SELECT t.name, ROUND(AVG(p.weight),2) as Average_weight , ROUND(AVG(p.height),2) as Average_height
FROM dim_pokemon p
JOIN fact_pokemon_type ft
ON ft.pokemon_id = p.pokemon_id
    JOIN dim_type t
    ON ft.type_id = t.type_id
GROUP BY t.name

-- Pokemon with multiple types
SELECT p.name, COUNT(t.name)
FROM dim_pokemon p
JOIN fact_pokemon_type ft
ON ft.pokemon_id = p.pokemon_id
    JOIN dim_type t
    ON ft.type_id = t.type_id
GROUP BY p.name
HAVING count(t.name) > 1
ORDER BY p.name