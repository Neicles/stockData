SELECT DISTINCT
    id AS subscriber_id,
    LOWER(TRIM(login)) AS subscriber_login,
    avatar_url,
    html_url,
    type AS user_type,
    site_admin
FROM {{ source('github_data', 'subscribers_data') }}
WHERE login IS NOT NULL
