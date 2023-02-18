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


global num
num = 0


def run_bot():

    TOKEN = open('SettingsFile//token.txt').read()

    if not TOKEN:
        print("Token is not definde")
        exit(1)

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    button1 = KeyboardButton('Знаю')
    button2 = KeyboardButton('Не знаю')
    button3 = KeyboardButton('Закончить')
    button4 = KeyboardButton('Далее')
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
        button1, button2).add(button3)
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        button4).add(button3)

    @dp.message_handler(commands=["start"])
    async def command_start_handler(msg: types.Message):
        await msg.answer(f"Hello {msg.from_user.first_name} Написать краткую информацию", reply_markup=ReplyKeyboardRemove())
        add_users(msg.from_user.id, date.today())

    @dp.message_handler(commands=["help"])
    async def command_help_handler(msg: types.Message):
        await msg.answer(f"Информация", reply_markup=ReplyKeyboardRemove())

    @dp.message_handler(commands=["go"])
    async def command_go_handler(msg: types.Message):
        num = randint(0, 499)
        dif = 3
        await msg.answer(f"{sql_word(num, msg.from_user.id,dif)}", reply_markup=keyboard1)
    # решить что то с num
    # с dif решить
    # сделать кнопку далее

    @dp.message_handler()
    async def word_handler(msg: types.Message):
        if msg.text == 'Знаю':
            conn = sqlite3.connect(f'UsersData\\{msg.from_user.id}.db')
            cur = conn.cursor()
            cur.execute(f"UPDATE word SET difficulty=difficulty-1 WHERE id == {num} and difficulty >0")
            cur.execute(f"SELECT * FROM word WHERE difficulty == {dif}")

            word = cur.fetchall()[num]
            word_en = (word[1])
            word_ru = (word[2])
            word_dif = (word[3])
            conn.commit()
            await  msg.answer(f"{word_en} - {word_ru}\nТекущая сложность слова = {word_dif}",  reply_markup=keyboard2)
            

        elif msg.text == 'Не знаю':

            num, dif = 1, 3

            conn = sqlite3.connect(f'UsersData\\{msg.from_user.id}.db')
            cur = conn.cursor()
            cur.execute(f"UPDATE word SET difficulty=difficulty+1 WHERE id == {num} and difficulty <5")
            cur.execute(f"SELECT * FROM word WHERE difficulty == {dif}")

            word = cur.fetchall()[num]
            word_en = (word[1])
            word_ru = (word[2])
            word_dif = (word[3])

            conn.commit()

            await  msg.answer(f"{word_en} - {word_ru}\nТекущая сложность слова = {word_dif}",  reply_markup=keyboard2)
            
        elif msg.text == "Далее":
        	num = randint(0, 499)
        	dif = 3
        	await msg.answer(f"{sql_word(num, msg.from_user.id,dif)}", reply_markup=keyboard1)


        elif (msg.text == "Закончить") or (msg.text ==  "/stop") or (msg.text ==  "/end"):
            await msg.answer(f"Спасибо за тест", reply_markup=ReplyKeyboardRemove())

        
    executor.start_polling(dp, skip_updates=True)


def sql_word(rand, num, dif=-1):

    conn = sqlite3.connect(f'UsersData\\{num}.db')
    cur = conn.cursor()

    if dif >= 1 and dif <= 5:
        cur.execute(f"SELECT * FROM word WHERE difficulty == {dif}")

    else:
        cur.execute(f"SELECT * FROM word")

    word = cur.fetchall()[rand][1]
    conn.commit()
    return (word)
