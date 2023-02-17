
# from CopyWord import *
from UserDB import create_UsersDB
from tgBot import run_bot


#все закоменченные файлы стоит запускать перед первым запуском

if __name__ == "__main__":
	# create_WordDB()
	# download_word()
	create_UsersDB()

	

	run_bot()
