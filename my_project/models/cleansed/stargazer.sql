SELECT
    id AS stargazer_id,
    login AS user_login,
    avatar_url,
    html_url,
    type AS user_type,
    site_admin
FROM {{ source('github_data', 'stargazers_data') }}
