import psycopg2
from faker import Faker
import random

# Налаштування підключення до PostgreSQL
DB_NAME = "task_1_db"
DB_USER = "postgres"
DB_PASSWORD = "pass"
DB_HOST = "localhost"
DB_PORT = "5432"

# Підключення до бази даних
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Функція для заповнення таблиці users
def seed_users(n):
    for _ in range(n):
        fullname = fake.name()
        email = fake.email()
        cursor.execute('''
        INSERT INTO users (fullname, email)
        VALUES (%s, %s)
        ''', (fullname, email))
    conn.commit()
    print(f"Inserted {n} users into the users table")

# Функція для заповнення таблиці tasks
def seed_tasks(n):
    cursor.execute('SELECT id FROM users')
    user_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT id FROM status')
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute('''
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (%s, %s, %s, %s)
        ''', (title, description, status_id, user_id))
    conn.commit()
    print(f"Inserted {n} tasks into the tasks table")

if __name__ == "__main__":
    # Заповнення таблиці users 10 випадковими користувачами
    seed_users(10)
    
    # Заповнення таблиці tasks 20 випадковими завданнями
    seed_tasks(20)

    # Закриття підключення до бази даних
    cursor.close()
    conn.close()
