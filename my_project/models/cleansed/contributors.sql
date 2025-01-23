SELECT DISTINCT
    id AS contributor_id,
    LOWER(TRIM(login)) AS contributor_login,  -- Normalisation : login en minuscule, suppression des espaces
    contributions AS nombre_contributions
FROM {{ source('github_data', 'contributors_data') }}
WHERE login IS NOT NULL
  AND contributions > 0
