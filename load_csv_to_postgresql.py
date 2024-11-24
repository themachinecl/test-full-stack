import pandas as pd
import psycopg2

DB_CONFIG = {
    "host": "localhost",      
    "database": "postgres",   
    "user": "postgres",       
    "password": "postgres"    
}

SQL_FILE = "initbd.sql"
SCHEMA = "public_test_full_stack"  

with open(SQL_FILE, "r") as file:
    sql_script = file.read().replace("{{schema}}", SCHEMA)

def execute_sql_file(sql_script):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()
        print("Script OK!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def load_csv_to_postgresql(csv_file_path, table_name, schema):
    try:
        df = pd.read_csv(csv_file_path)
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        for _, row in df.iterrows():
            columns = ", ".join(df.columns)
            values = ", ".join(["%s"] * len(row))
            query = f"INSERT INTO {schema}.{table_name} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(row))
        conn.commit()
        print(f"Data OK'{schema}.{table_name}' to '{csv_file_path}'.")

    except Exception as e:
        print(f"Error Data '{schema}.{table_name}': {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

FILES_AND_TABLES = [
    ("Test task - Postgres - customer_companies.csv", "customer_companies"),
    ("Test task - Postgres - customers.csv", "customers"),
    ("Test task - Postgres - deliveries.csv", "deliveries"),
    ("Test task - Postgres - order_items.csv", "order_items"),
    ("Test task - Postgres - orders.csv", "orders"),
]

print(f"run... '{SQL_FILE}'...")
execute_sql_file(sql_script)

for file_path, table_name in FILES_AND_TABLES:
    print(f"Load '{file_path}' to Tabl '{table_name}'...")
    load_csv_to_postgresql(file_path, table_name, SCHEMA)
