import requests
from bs4 import BeautifulSoup
import sqlite3


def download_word():
	conn = sqlite3.connect('WordsTable.db')
	cur = conn.cursor()

	url = open('Link.txt','r').read()

	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'lxml')

	names = soup.find_all('tr')

	for _ in names:

		data = _.find_all('td')

		list_words = []
		for index in data:
			list_words.append(index.text)

		cur.execute("INSERT INTO word VALUES(?, ?, ?);", list_words)

	conn.commit()			



	


	


def create_bd():

	conn = sqlite3.connect('WordsTable.db')

	cur = conn.cursor()
	
	cur.execute("""CREATE TABLE IF NOT EXISTS word(
   		id INT,
   		enWord TEXT,
   		ruWord TEXT);
	""")

	conn.commit()
