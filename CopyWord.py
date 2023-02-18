import requests
from bs4 import BeautifulSoup
import sqlite3
import os


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
        cur.execute(f"INSERT INTO word VALUES(?, ?, ?, {basic_difficulty});", list_words)

    conn.commit()


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
		difficulty INT);
	""")

    conn.commit()
