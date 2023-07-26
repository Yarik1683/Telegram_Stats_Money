import sqlite3

try:
    conn = sqlite3.connect("accountant.db", check_same_thread=True)
    cursor = conn.cursor()

    # Создание таблицы 'users' с полем 'user_id'
    cursor.execute("CREATE TABLE IF NOT EXISTS 'users' ('user_id' INTEGER PRIMARY KEY)")

    # Считываем всех пользователей
    users = cursor.execute("SELECT * FROM 'users'")
    print(users.fetchall())

except sqlite3.Error as error:
    print("Ошибка", error)

finally:
    if conn:
        conn.close()
