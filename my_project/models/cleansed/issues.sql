SELECT
    id AS issue_id,
    number AS issue_number,
    title AS issue_title,
    user ->> 'id' AS contributor_id,
    user ->> 'login' AS contributor_login,
    state AS issue_state,
    created_at::DATE AS issue_created_date,
    updated_at::DATE AS issue_updated_date,
    closed_at::DATE AS issue_closed_date,
    comments AS issue_comments_count
FROM {{ source('github_data', 'issues_data') }}
WHERE state IS NOT NULL
