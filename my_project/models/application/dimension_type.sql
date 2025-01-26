SELECT DISTINCT
    CASE
        WHEN LOWER(issue_title) LIKE '%bug%' THEN 1
        WHEN LOWER(issue_title) LIKE '%feature%' OR LOWER(issue_title) LIKE '%enhancement%' THEN 2
        WHEN LOWER(issue_title) LIKE '%doc%' OR LOWER(issue_title) LIKE '%documentation%' THEN 3
        ELSE 4
    END AS id_type,
    CASE
        WHEN LOWER(issue_title) LIKE '%bug%' THEN 'Bug'
        WHEN LOWER(issue_title) LIKE '%feature%' OR LOWER(issue_title) LIKE '%enhancement%' THEN 'Feature'
        WHEN LOWER(issue_title) LIKE '%doc%' OR LOWER(issue_title) LIKE '%documentation%' THEN 'Documentation'
        ELSE 'Autre'
    END AS type
FROM {{ ref('issues') }}
WHERE issue_title IS NOT NULL
ORDER BY id_type
