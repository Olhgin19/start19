import sqlite3


def add_user(db_path, name, email, password):
    """
    Функция для добавления нового пользователя в базу данных.
    :param db_path: Путь к файлу базы данных SQLite
    :param name: Имя пользователя
    :param email: Email пользователя
    :param password: Пароль пользователя
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Регистрация (Name, Email, Password) VALUES (?, ?, ?)
        """, (name, email, password))

        conn.commit()
        print("Пользователь успешно добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении пользователя: {e}")
    finally:
        conn.close()

def get_all_users(db_path):
    """
    Функция для получения всех пользователей из базы данных.
    :param db_path: Путь к файлу базы данных SQLite
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Регистрация")
        users = cursor.fetchall()
        
        print("Список пользователей:")
        for user in users:
            print(user)
    except sqlite3.Error as e:
        print(f"Ошибка при получении пользователей: {e}")
    finally:
        conn.close()

def login(db_path, email, password):
    """
    Функция для проверки входа пользователя в систему.
    :param db_path: Путь к файлу базы данных SQLite
    :param email: Email пользователя
    :param password: Пароль пользователя
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Регистрация WHERE Email = ? AND Password = ?", (email, password))
        user = cursor.fetchone()
        
        if user:
            print("Вход выполнен успешно!")
        else:
            print("Неверный email или пароль.")
    except sqlite3.Error as e:
        print(f"Ошибка при проверке входа: {e}")
    finally:
        conn.close()

# Проверка входа
login("D:\\DB\\my_database.db", "gena1@example.com", "mypassword123")
login("D:\\DB\\my_database.db", "olhgin899@gmail.com", "wrongpassword")



