# English-Bot

ПЛАН:

English Bot

1. Создание парсера, который с сайта (https://studynow.ru/dicta/allwords) выкачиват слова, и сохранит ее в sql-lite таблицу. +
 - План Таблицы:
	userid  word translate difficulty(по стандарту 3, каждый ответ изменяет сложность изменяется (min 1, max 5)  
	
2. Програма-успраженение, которое имеет 2 команды:
	- /start
	- /end
	И так же входные данные(сложность слов, диапозон или что то подобное) + Выбор языка (en/ru) для выводимого слова
	
	Суть:
	
	Выходит, слов на анг/рус и рядом его сложность. У человека 3 кнопки => {знаю} - напишите слово, 
																					-если оно идеально совпало, то дальше + сложность слова уменьшается
																					-если не совпало, у человека 2 кнопки + виден перевод, данное слово + уровень сложность => {правильно}, сложность слова уменьшается и идем дальше
																																												{неправильно},показ перевода, сложность слова увеличивается и идем дальше
																					
																			{не знаю} -  Показ перевода, сложность слова увеличивается и идем дальше
																			
	
	Из необходимых функций:
	 - слов в таком диопозоне нет
	 -
	 
3. Создание все это в тг + его оформление
4. Поднять его на сервере


Доп функции в телеграме:
 - создание словаря с избранными словами (добавление новой кнопки во все пункты)
 -скачать таблицу со словами



Доп навыки за время создание проекта: 
	-освоение git
	-улучшение англиского
	-закрепление работы с парсингом, ботом и sql
	
Будущее: 
	-приложение с интерфесом для windows
	-приложение на android
	-онлайн версия
	-сайт со всей необходимой информацией
