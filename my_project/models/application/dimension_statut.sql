SELECT
    DENSE_RANK() OVER (ORDER BY issue_state) AS id_statut,
    issue_state AS statut,
    CONCAT('ticket: ', issue_state) AS description
FROM {{ ref('issues') }}
WHERE issue_state IS NOT NULL
GROUP BY issue_state
