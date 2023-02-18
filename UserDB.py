import sqlite3
import os
import shutil

# Функция,которая проверяет наличие собственой таблицы пользователя, при отсутвие создает её. Так же сохраняет каждый id и дату регестрации пользователя в Админ Таблицу
def add_users(num, dat):
    conn = sqlite3.connect(r'AdminFolder\Users.db')
    cur = conn.cursor()

    i = [num, dat]

    cur.execute(f"SELECT * FROM users WHERE id == {num} ")

    if (cur.fetchall()):
        conn.commit()

        return 0

    cur.execute("INSERT INTO users VALUES(?, ?);", i)
    conn.commit()
    try:
        os.mkdir('UsersData')

    except:
        pass

    src = r'AdminFolder\WordsTable.db'
    dest = r'UsersData'

    shutil.copy2(src, dest)

    os.rename(r'UsersData\WordsTable.db', f'UsersData\\{str(num)+".db"}')


# создание таблицы c ID пользователей
def create_UsersDB():

    try:
        os.mkdir("AdminFolder")
    except:
        pass

    conn = sqlite3.connect(r'AdminFolder\Users.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INT,
        dat TEXT);
    """)

    conn.commit()
