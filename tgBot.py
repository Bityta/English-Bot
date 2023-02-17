from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from UserDB import add_users
import datetime


def run_bot():
	TOKEN = open('SettingsFile//token.txt').read()

	if not TOKEN:
		print ("Token is not definde")
		exit(1)

	bot = Bot(token = TOKEN)
	dp = Dispatcher(bot)

	@dp.message_handler(commands=["start"])
	async def command_start_handler(msg : types.Message):
		await msg.answer(f"Приветвую {msg.from_user.first_name} ДОПИСАТЬ ТЕКСТ!")

		add_users(msg.from_user.id, "2023-12-12")
		
		
		

	@dp.message_handler()
	async def echo(msg : types.Message):
		await msg.answer(msg.text)






	executor.start_polling(dp,skip_updates = True)

