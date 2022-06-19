import psycopg2
from config import host, user, password, db_name


try:
    # Подключение к базе данных
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True 
    
    # Получение версии бд
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    # Создание 
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);"""
        )

        print("[INFO] Tabel created successfylly")

    # Заполнение
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, nick_name)
                VALUES ('Maxim', 'Dragon');"""
        )

        print("[INFO] Data was successfylly inserted")

    # Извеление записи
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name from users
            WHERE first_name = 'Maxim';"""
        )

        print("[INFO] Result selected:", cursor.fetchone()[0])  

    # Удаление 
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users"""
        )

        print("[INFO] Database deleted")

except Exception as _ex:
    print("[INFO] Error:", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")