import duckdb

# Connexion à une base DuckDB persistante (au lieu d'in-memory)
db_path = "dbStockData.duckdb"
with duckdb.connect(db_path) as con:
    # Créer le schéma raws
    con.execute("CREATE SCHEMA IF NOT EXISTS raws")

    def create_and_read_table_from_parquet_file(con, parquet_file, schema_name, table_name):
        con.execute(f"CREATE OR REPLACE TABLE {schema_name}.{table_name} AS SELECT * FROM read_parquet('{parquet_file}')")
        result = con.execute(f"SELECT * FROM {schema_name}.{table_name}").fetchdf()
        return result

    contributors_data = create_and_read_table_from_parquet_file(con, 'data/contributors_data.parquet', 'raws', 'contributors_data')
    print(contributors_data)

    forks_data = create_and_read_table_from_parquet_file(con, 'data/forks_data.parquet', 'raws', 'forks_data')
    print(forks_data)

    issues_data = create_and_read_table_from_parquet_file(con, 'data/issues_data.parquet', 'raws', 'issues_data')
    print(issues_data)

    suscribers_data = create_and_read_table_from_parquet_file(con, 'data/subscribers_data.parquet', 'raws', 'subscribers_data')
    print(suscribers_data)

    stargazers_data = create_and_read_table_from_parquet_file(con, 'data/stargazers_data.parquet', 'raws', 'stargazers_data')
    print(stargazers_data)
