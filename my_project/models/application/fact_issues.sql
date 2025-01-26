WITH issue_data AS (
    SELECT DISTINCT ON (issues.issue_id)
        issues.issue_id,
        issues.issue_number,
        issues.issue_title,
        issues.issue_state,
        COALESCE(dim_statut.id_statut, -1) AS id_statut,
        COALESCE(dim_date_creation.id_date, DATE '1970-01-01') AS id_date_creation,
        COALESCE(dim_date_update.id_date, DATE '1970-01-01') AS id_date_update,
        COALESCE(dim_date_cloture.id_date, DATE '1970-01-01') AS id_date_cloture,
        issues.issue_comments_count,
        issues.contributor_id,
        COALESCE(dim_type.id_type, 4) AS id_type,
        COALESCE(dim_priorite.id_priorite, 3) AS id_priorite
    FROM {{ ref('issues') }} AS issues
    LEFT JOIN {{ ref('dimension_statut') }} AS dim_statut
        ON issues.issue_state = dim_statut.statut
    LEFT JOIN {{ ref('dimension_date') }} AS dim_date_creation
        ON issues.issue_created_date = dim_date_creation.id_date
    LEFT JOIN {{ ref('dimension_date') }} AS dim_date_update
        ON issues.issue_updated_date = dim_date_update.id_date
    LEFT JOIN {{ ref('dimension_date') }} AS dim_date_cloture
        ON issues.issue_closed_date = dim_date_cloture.id_date
    LEFT JOIN {{ ref('dimension_type') }} AS dim_type
        ON CASE
            WHEN LOWER(issues.issue_title) LIKE '%bug%' THEN 1
            WHEN LOWER(issues.issue_title) LIKE '%feature%' OR LOWER(issues.issue_title) LIKE '%enhancement%' THEN 2
            WHEN LOWER(issues.issue_title) LIKE '%doc%' OR LOWER(issues.issue_title) LIKE '%documentation%' THEN 3
            ELSE 4
        END = dim_type.id_type
    LEFT JOIN {{ ref('dimension_priorite') }} AS dim_priorite
        ON CASE
            WHEN issues.issue_comments_count > 10 THEN 3
            WHEN issues.issue_comments_count BETWEEN 3 AND 10 THEN 2
            ELSE 1
        END = dim_priorite.id_priorite
)
SELECT
    COUNT(issue_id) AS total_issues,
    AVG(DATEDIFF('day', CAST(id_date_creation AS DATE), COALESCE(CAST(id_date_cloture AS DATE), CURRENT_DATE))) AS avg_resolution_time_days,
    (COUNT(CASE WHEN issue_state = 'closed' THEN 1 END) * 100.0 / COUNT(issue_id)) AS resolution_percentage,
    SUM(CASE WHEN id_priorite = 3 THEN 1 ELSE 0 END) AS critical_issues,
    SUM(CASE WHEN id_priorite = 2 THEN 1 ELSE 0 END) AS high_issues,
    SUM(CASE WHEN id_priorite = 1 THEN 1 ELSE 0 END) AS low_issues,
    COUNT(DISTINCT id_type) AS distinct_types,
    COUNT(DISTINCT contributor_id) AS distinct_responsibles
FROM issue_data
