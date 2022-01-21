import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
api = requests.get("https://IQhost.xyz/Phone").json()["result"]
n = api[1]
n1 = api[2]
n2 = api[3]
n3 = api[4]
n4 = api[5]
ss = types.InlineKeyboardButton(text=f"- Num : {n}",callback_data="s")
ss1 = types.InlineKeyboardButton(text=f"- Num : {n1}",callback_data="s1")
ss2 = types.InlineKeyboardButton(text=f"- Num : {n2}",callback_data="s2")
ss3 = types.InlineKeyboardButton(text=f"- Num : {n3}",callback_data="s3")
ss4 = types.InlineKeyboardButton(text=f"- Num : {n4}",callback_data="s4")
de = types.InlineKeyboardButton(text=f"- Update Numbers ",callback_data="d")
bot = telebot.TeleBot(tok)
dev = types.InlineKeyboardButton(text="- Dev ",url="https://t.me/uufffuu")
@bot.message_handler(commands=["start"])
def start_welcome(message):
	name = message.chat.first_name
	u = "https://t.me/pydroi_d_3/40"
	key = types.InlineKeyboardMarkup()
	key.row_width=1
	key.add(ss,ss1,ss2,ss3,ss4,de,dev)
	bot.send_photo(message.chat.id,u,f"""
=== === === ===
- Hi {name}
- Welcome Bot Fake Number 
- Choice Numper 
=== === === ===
- ᴅᴇᴠ -@uufffuu""",reply_markup=key)
@bot.callback_query_handler(func=lambda call :True)
def f(call):
	if call.data=="s":
		st(call.message)
	if call.data=="s1":
		st1(call.message)
	if call.data=="s2":
		st2(call.message)
	if call.data=="s3":
		st3(call.message)
	if call.data=="s4":
		st4(call.message)
	if call.data=="d":
		st5(call.message)
def st4(message):
	api = requests.get(f"https://IQhost.xyz/Phone/{n4}").text
	if '"last_Message":null' in api:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n4}
- Message : No Messages
=== === === ===""")
	else:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n4}
- Message : {api}
=== === === ===""")
def st3(message):
	api = requests.get(f"https://IQhost.xyz/Phone/{n3}").text
	if '"last_Message":null' in api:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n3}
- Message : No Messages
=== === === ===""")
	else:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n3}
- Message : {api}
=== === === ===""")
def st2(message):
	api = requests.get(f"https://IQhost.xyz/Phone/{n2}").text
	if '"last_Message":null' in api:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n2}
- Message : No Messages
=== === === ===""")
	else:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n2}
- Message : {api}
=== === === ===""")
def st1(message):
	api = requests.get(f"https://IQhost.xyz/Phone/{n1}").text
	if '"last_Message":null' in api:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n1}
- Message : No Messages
=== === === ===""")
	else:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n1}
- Message : {api}
=== === === ===""")
def st(message):
	api = requests.get(f"https://IQhost.xyz/Phone/{n}").text
	if '"last_Message":null' in api:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n}
- Message : No Messages
=== === === ===""")
	else:
		bot.send_message(message.chat.id,f"""
=== === === ===
- Numper : {n}
- Message : {api}
=== === === ===""")
def st5(message):
	bot.send_message(message.chat.id,"- Update Number \n- Send /start\n- Dev @uufffuu")
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://sidrabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))