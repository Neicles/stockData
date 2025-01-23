SELECT
    id,
    name,
    full_name,
    owner ->> 'login' AS owner_login,
    forks_count,
    archived,
    disabled,
    CAST(created_at AS DATE) AS created_at,
    CAST(updated_at AS DATE) AS updated_at
FROM {{ source('github_data', 'forks_data') }}
WHERE archived = FALSE
  AND disabled = FALSE