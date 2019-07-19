# -*- coding: utf-8 -*-

import telebot, logging, os
from consts import users

WORKDIR = "./"
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
API_TOKEN = os.environ['TELEGRAM_TOKEN']
print(API_TOKEN)

bot = telebot.TeleBot(API_TOKEN)
known_users = []

with open(os.path.join(WORKDIR, 'files/known_users.txt'), mode='r',encoding='utf-8') as f:
	for line in f:
		known_users.append(int(line.split("#")[0].strip()))

@bot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	if cid not in known_users:
		bot.send_message(cid,"Seja bem vindo!")
		with open(os.path.join(WORKDIR, 'files/known_users.txt'), mode='w',encoding='utf-8') as f:
			f.write(cid+" # "+m.chat.username)
			known_users.append(cid)

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
	cid = m.chat.id
	with open(os.path.join(WORKDIR, 'files/help_file.txt'), 'r', encoding='utf-8') as help_file:
		help_text = help_file.read()
	bot.send_message(cid, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['pikachu'])
def command_pikachu(m):
	cid = m.chat.id
	bot.send_chat_action(cid,'upload_photo')
	bot.send_photo(cid,"AgADAQADeqgxG9ZaiEU6myK6BPNQjsp2DDAABH83Oz3z1ILBWZgFAAEC")

@bot.message_handler(commands=['zbetho'])
def command_zbetho(m):
	cid = m.chat.id
	bot.send_chat_action(cid,'record_audio')
	bot.send_audio(cid,"CQADAQADWQAD1lqIRUGBFz-w2AGdAg")

@bot.message_handler(commands=['iutubi'])
def command_iutubi(m):
	cid = m.chat.id
	bot.forward_message(cid, users["silver"], 15)

@bot.message_handler(commands=['pqp'])
def command_pqp(m):
	cid = m.chat.id
	bot.send_chat_action(cid,'record_audio')
	bot.forward_message(cid,users["silver"],18)
	bot.forward_message(cid,users["silver"],19)

@bot.message_handler(commands=['oibb'])
def command_oibb(m):
	cid = m.chat.id
	bot.send_chat_action(cid,'record_audio')
	bot.send_voice(cid,"AwADBAADDAEAAhaglFPTHE39AW2hKgI")

bot.polling(none_stop=False,interval=0,timeout=20)