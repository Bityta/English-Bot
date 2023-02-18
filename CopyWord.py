import requests
from bs4 import BeautifulSoup
import sqlite3
import os

#загрузка слов с сайта и запись их в базовую таблицу со словами
def download_word():
    # connecting DB
    conn = sqlite3.connect(r'AdminFolder\WordsTable.db')
    cur = conn.cursor()

    # парсер сайта
    url = open('SettingsFile//Link.txt', 'r').read()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    for _ in soup.find_all('tr'):

        data = _.find_all('td')

        list_words = []

        for index in data:
            list_words.append(index.text)

        basic_difficulty = 3
        cur.execute(f"INSERT INTO word VALUES(?, ?, ?, {basic_difficulty},NULL,NULL);", list_words)
        
    cur.execute(f"UPDATE word SET last_word = -1, last_difficulty = 3 WHERE id = 1;")

    conn.commit()

#Создание базовый таблицы содержащия индекс,анг слово, перевод, сложность(базовая сложность 3)
def create_WordDB():

    try:
        os.mkdir('AdminFolder')

    except:
        pass

    conn = sqlite3.connect(r'AdminFolder\WordsTable.db')

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS word(
   		id INT,
   		enWord TEXT,
   		ruWord TEXT,
		difficulty INT,
        last_word INT,
        last_difficulty INT);
	""")

    conn.commit()
