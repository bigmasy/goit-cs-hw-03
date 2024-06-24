import psycopg2
from psycopg2 import sql

# Налаштування підключення до PostgreSQL
DB_NAME = "task_1_db"
DB_USER = "postgres"
DB_PASSWORD = "pass"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_database():
    try:
        # Підключення до системної бази даних PostgreSQL
        conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        cursor = conn.cursor()

        # Створення нової бази даних
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
        
        cursor.close()
        conn.close()
        print(f"Database {DB_NAME} created successfully!")
    except Exception as e:
        print(f"Error creating database: {e}")

def create_tables(filename):
    try:
        # Підключення до новоствореної бази даних
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cursor = conn.cursor()

        # Читання SQL команд з файлу
        with open(filename, 'r') as file:
            sql_commands = file.read()

        # Виконання SQL команд
        cursor.execute(sql_commands)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")
if __name__ == "__main__":
    create_database()
    create_tables('users.sql')
