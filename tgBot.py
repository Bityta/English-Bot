from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from UserDB import add_users
from datetime import date
import sqlite3
from random import randint


def run_bot():

    TOKEN = open('SettingsFile//token.txt').read()

    if not TOKEN:
        print("Token is not definde")
        exit(1)

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    # создание кнопок и соеденение их в некую клавиатуру
    button1 = KeyboardButton('Знаю')
    button2 = KeyboardButton('Не знаю')
    button3 = KeyboardButton('Закончить')
    button4 = KeyboardButton('Далее')
    button5 = KeyboardButton('Инфо')
    button6 = KeyboardButton('Начать')
    button7 = KeyboardButton('Скрыть')
    button8 = KeyboardButton('хз')
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).row(
        button1, button2).add(button3)
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True).add(
        button4).add(button3)
    keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True).row(
        button6, button5).add(button8, button7)

    # стартовая команда, которая приветсвует пользователя и создает для него пользовательскую таблицу со словами, а так же вносит его id в Админ Таблицу
    @dp.message_handler(commands=["start"])
    async def command_start_handler(msg: types.Message):
        await msg.answer(f"Приветсвую {msg.from_user.first_name}. " +
                         "Хочешь проверить свой англиский словарный запас или выучить " +
                         "5000 самых популярных англиский слов?? " +
                         "Тогда ты пришел правильно.\nНачать - /go\n" +
                         "Подробная Информация - /help", reply_markup=ReplyKeyboardRemove())

        add_users(msg.from_user.id, date.today())

    # команда, информирущая пользователя о различной информации о Боте
    @dp.message_handler(commands=["help"])
    async def command_help_handler(msg: types.Message):
        await msg.answer(f"Информация ПОКА ЛЕНЬ ПИСАТЬ!!", reply_markup=ReplyKeyboardRemove())

    # команда, которая запускает Интерактивную часть Бота
    @dp.message_handler(commands=["go"])
    async def command_go_handler(msg: types.Message):
        await msg.answer(f"{sql_word(msg.from_user.id)}", reply_markup=keyboard1)

    # решить что то с num
    # с dif решить
    # сделать кнопку далее

    @dp.message_handler()
    async def word_handler(msg: types.Message):
        if msg.text == 'Знаю':
            conn = sqlite3.connect(f'UsersData\\{msg.from_user.id}.db')
            cur = conn.cursor()

            cur.execute(f"SELECT last_word FROM word WHERE id = 1")
            rand = (cur.fetchall()[0][0])

            cur.execute(f"UPDATE word SET difficulty=difficulty-1 WHERE id == {rand} and difficulty >0")

            cur.execute(f"SELECT enWord, ruWord, difficulty FROM word WHERE id == {rand}")

            word_en, word_ru, word_dif = cur.fetchall()[0]
            conn.commit()
            await  msg.answer(f"{word_en} - {word_ru}\nТекущая сложность слова - {word_dif}",  reply_markup=keyboard2)

        elif msg.text == 'Не знаю':

            conn = sqlite3.connect(f'UsersData\\{msg.from_user.id}.db')
            cur = conn.cursor()

            cur.execute(f"SELECT last_word FROM word WHERE id = 1")
            rand = (cur.fetchall()[0][0])

            cur.execute(f"UPDATE word SET difficulty=difficulty+1 WHERE id == {rand} and difficulty < 5")

            cur.execute(f"SELECT enWord, ruWord, difficulty FROM word WHERE id == {rand}")

            word_en, word_ru, word_dif = cur.fetchall()[0]
            conn.commit()
            await  msg.answer(f"{word_en} - {word_ru}\nТекущая сложность слова - {word_dif}",  reply_markup=keyboard2)

        elif msg.text == "Далее":
            await msg.answer(f"{sql_word(msg.from_user.id)}", reply_markup=keyboard1)

        elif msg.text == "Инфо":
            await msg.answer(f"Информация ПОКА ЛЕНЬ ПИСАТЬ!!", reply_markup=keyboard3)

        elif msg.text == "Начать":
            await msg.answer(f"{sql_word(msg.from_user.id)}", reply_markup=keyboard1)

        elif msg.text == "хз":
            await msg.answer(f"диман иди нахуй", reply_markup=keyboard3)

        elif msg.text == "Скрыть":

            await msg.answer_sticker(r'CAACAgIAAxkBAAEHzTpj8UxFqlX3fFV4ccNgoS7lBHl3AAMTIgAChpJJS6Z_IJsc_IGpLgQ')

        elif (msg.text == "Закончить") or (msg.text == "/stop") or (msg.text == "/end"):
            await msg.answer(f"Отлично позанимались! :)", reply_markup=keyboard3)

    executor.start_polling(dp, skip_updates=True)


def sql_word(num):

    conn = sqlite3.connect(f'UsersData\\{num}.db')
    cur = conn.cursor()

    rand = randint(1, 500)
    cur.execute(f"UPDATE word SET last_word = {rand} WHERE id = 1;")

    cur.execute(f"SELECT last_difficulty,last_word FROM word WHERE id = 1")

    dif, rand = (cur.fetchall()[0])

    if dif >= 1 and dif <= 5:
        cur.execute(f"SELECT enWord FROM word WHERE difficulty == {dif}")

    else:
        cur.execute(f"SELECT enWord FROM word")

    word = cur.fetchall()[rand-1][0]

    conn.commit()
    return (word)
