import requests
from bs4 import BeautifulSoup
import sqlite3


def download_word():
	#подключение к БД
	conn = sqlite3.connect('WordsTable.db')
	cur = conn.cursor()

	#парсер сайта
	url = open('Link.txt','r').read()
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml') 

	for _ in soup.find_all('tr'):

		data = _.find_all('td')

		list_words = []

		for index in data:
			list_words.append(index.text)

		#difficulty basic = 3
		cur.execute("INSERT INTO word VALUES(?, ?, ?, 3);", list_words)

	conn.commit()			


def create_bd():

	conn = sqlite3.connect('WordsTable.db')

	cur = conn.cursor()
	
	cur.execute("""CREATE TABLE IF NOT EXISTS word(
   		id INT,
   		enWord TEXT,
   		ruWord TEXT,
		difficulty INT);
	""")

	conn.commit()
