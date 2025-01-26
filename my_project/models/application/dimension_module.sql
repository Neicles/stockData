SELECT DISTINCT
    DENSE_RANK() OVER (ORDER BY module) AS id_module,
    module
FROM (
    SELECT DISTINCT
        CASE
            WHEN issue_title LIKE '%:%' THEN TRIM(SPLIT_PART(issue_title, ':', 1))
            ELSE 'Autre'
        END AS module
    FROM {{ ref('issues') }}
    WHERE issue_title IS NOT NULL
) subquery
