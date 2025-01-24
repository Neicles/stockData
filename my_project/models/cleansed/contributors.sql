SELECT DISTINCT
    id AS contributor_id,
    LOWER(TRIM(login)) AS contributor_login,
    contributions AS nombre_contributions
FROM {{ source('github_data', 'contributors_data') }}
WHERE login IS NOT NULL
  AND contributions > 0
