import pandas as pd
import psycopg2

# Configuración de la conexión a PostgreSQL
DB_CONFIG = {
    "host": "localhost",       # Cambia esto por tu host
    "database": "postgres",    # Nombre de tu base de datos
    "user": "postgres",        # Tu usuario
    "password": "postgres"     # Tu contraseña
}

# Función para ejecutar el script SQL desde un archivo
def execute_sql_file(sql_file_path):
    try:
        # Conectar a la base de datos PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Leer el contenido del archivo SQL
        with open(sql_file_path, 'r') as file:
            sql_commands = file.read()

        # Ejecutar el contenido del archivo SQL
        cursor.execute(sql_commands)

        # Confirmar los cambios
        conn.commit()
        print(f"Script SQL ejecutado exitosamente desde '{sql_file_path}'.")

    except Exception as e:
        print(f"Error al ejecutar el script SQL desde '{sql_file_path}': {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

# Función para cargar un archivo CSV en una tabla PostgreSQL
def load_csv_to_postgresql(csv_file_path, table_name):
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
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(row))

        # Confirmar los cambios
        conn.commit()
        print(f"Datos insertados exitosamente en la tabla '{table_name}' desde '{csv_file_path}'.")

    except Exception as e:
        print(f"Error al insertar los datos en la tabla '{table_name}': {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

# Nombre del archivo SQL para inicializar la base de datos
SQL_FILE = "initbd.sql"

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
execute_sql_file(SQL_FILE)

# Cargar cada archivo CSV en su tabla correspondiente
for file_path, table_name in FILES_AND_TABLES:
    print(f"Cargando datos desde '{file_path}' a la tabla '{table_name}'...")
    load_csv_to_postgresql(file_path, table_name)
