SELECT DISTINCT
    CAST(issues.contributor_id AS INTEGER) AS id_responsable,
    LOWER(TRIM(issues.contributor_login)) AS nom,
    'Contributeur' AS role
FROM {{ ref('issues') }} AS issues
LEFT JOIN {{ ref('contributors') }} AS contributors
    ON contributors.contributor_id = issues.contributor_id
WHERE issues.contributor_id IS NOT NULL
