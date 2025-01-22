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