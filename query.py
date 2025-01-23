import duckdb

# Connect to an in-memory DuckDB database
con = duckdb.connect()

def create_and_read_table_from_parquet_file(con, parquet_file, table_name):
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM '{parquet_file}'")
    result = con.execute(f"SELECT * FROM {table_name}").fetchdf()
    return result

# Read the contributors data from the parquet file
contributors_data = create_and_read_table_from_parquet_file(con, 'data/contributors_data.parquet', 'contributors_data')
print(contributors_data)

# Read the forks data from the parquet file
forks_data = create_and_read_table_from_parquet_file(con, 'data/forks_data.parquet', 'forks_data')
print(forks_data)

# Read the issues data from the parquet file
issues_data = create_and_read_table_from_parquet_file(con, 'data/issues_data.parquet', 'issues_data')
print(issues_data)

# Read the suscribers data from the parquet file
suscribers_data = create_and_read_table_from_parquet_file(con, 'data/suscribers_data.parquet', 'suscribers_data')
print(suscribers_data)

# Read the stargazers data from the parquet file
stargazers_data = create_and_read_table_from_parquet_file(con, 'data/stargazers_data.parquet', 'stargazers_data')
print(stargazers_data)