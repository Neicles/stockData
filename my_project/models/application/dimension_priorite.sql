SELECT DISTINCT
    CASE
        WHEN issue_comments_count > 10 THEN 3
        WHEN issue_comments_count BETWEEN 3 AND 10 THEN 2
        ELSE 1
    END AS id_priorite,
    CASE
        WHEN issue_comments_count > 10 THEN 'Haute'
        WHEN issue_comments_count BETWEEN 3 AND 10 THEN 'Moyenne'
        ELSE 'Basse'
    END AS priorite
FROM {{ ref('issues') }}
WHERE issue_comments_count IS NOT NULL
ORDER BY id_priorite
