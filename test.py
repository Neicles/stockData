import duckdb
import os

db_path = "dbStockData.duckdb"
with duckdb.connect(db_path) as con:

    query = """
    SELECT *
    FROM cleansed_application.fact_issues;
    """
    df_fact_issues = con.execute(query).fetchdf()

print("\nToutes les données de `fact_issues` :\n", df_fact_issues)

df_fact_issues.to_csv('fact_issues_full_data.csv', index=False)

df_fact_issues.to_csv('fact_issues_full_data.csv', index=False)

os.startfile('fact_issues_full_data.csv')

