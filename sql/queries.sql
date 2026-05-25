SELECT endpoint, resource_id, status_code, fetched_at
FROM raw_api_responses
ORDER BY resource_id;

SELECT COUNT(*)
FROM raw_api_responses;