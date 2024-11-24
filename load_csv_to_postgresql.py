import pandas as pd
import psycopg2

# Configuración de la conexión a PostgreSQL
DB_CONFIG = {
    "host": "localhost",       # Cambia esto por tu host
    "database": "postgres",    # Nombre de tu base de datos
    "user": "postgres",        # Tu usuario
    "password": "postgres"     # Tu contraseña
}

# Nombre del archivo SQL para inicializar la base de datos
SQL_FILE = "initbd.sql"
SCHEMA = "public_test_full_stack"  # Cambia este esquema según lo que necesites

# Leer el archivo SQL y reemplazar el marcador de esquema
with open(SQL_FILE, "r") as file:
    sql_script = file.read().replace("{{schema}}", SCHEMA)

# Función para ejecutar el script SQL desde un archivo
def execute_sql_file(sql_script):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()
        print("Script ejecutado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Función para cargar un archivo CSV en una tabla PostgreSQL
def load_csv_to_postgresql(csv_file_path, table_name, schema):
    try:
        # Leer el archivo CSV con pandas
        df = pd.read_csv(csv_file_path)

        # Conectar a la base de datos PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Iterar por cada fila del DataFrame e insertarla en la tabla
        for _, row in df.iterrows():
            # Construir el query de inserción dinámicamente según las columnas
            columns = ", ".join(df.columns)
            values = ", ".join(["%s"] * len(row))
            query = f"INSERT INTO {schema}.{table_name} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(row))

        # Confirmar los cambios
        conn.commit()
        print(f"Datos insertados exitosamente en la tabla '{schema}.{table_name}' desde '{csv_file_path}'.")

    except Exception as e:
        print(f"Error al insertar los datos en la tabla '{schema}.{table_name}': {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

# Lista de archivos CSV y las tablas correspondientes
FILES_AND_TABLES = [
    ("Test task - Postgres - customer_companies.csv", "customer_companies"),
    ("Test task - Postgres - customers.csv", "customers"),
    ("Test task - Postgres - deliveries.csv", "deliveries"),
    ("Test task - Postgres - order_items.csv", "order_items"),
    ("Test task - Postgres - orders.csv", "orders"),
]

# Ejecutar el script SQL para crear las tablas
print(f"Ejecutando el script SQL desde '{SQL_FILE}'...")
execute_sql_file(sql_script)

# Cargar cada archivo CSV en su tabla correspondiente
for file_path, table_name in FILES_AND_TABLES:
    print(f"Cargando datos desde '{file_path}' a la tabla '{table_name}'...")
    load_csv_to_postgresql(file_path, table_name, SCHEMA)
