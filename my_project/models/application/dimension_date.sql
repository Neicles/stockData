WITH date_data AS (
    SELECT DISTINCT
        issue_created_date AS id_date,
        EXTRACT(DAY FROM issue_created_date) AS jour,
        EXTRACT(MONTH FROM issue_created_date) AS mois,
        EXTRACT(YEAR FROM issue_created_date) AS annee
    FROM {{ ref('issues') }}
    WHERE issue_created_date IS NOT NULL
)
SELECT * FROM date_data
