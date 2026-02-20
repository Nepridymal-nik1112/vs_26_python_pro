import telebot
import random
import re
from main1 import password
from main1 import coins
bot = telebot.TeleBot("TOKEN")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_pass(message):
       bot.reply_to(message, password())


@bot.message_handler(commands=['arithmetika'])
def send_math_plus(message):
     t = message.text.replace('/arithmetika', '').strip()
     if not re.match(r"^[0-9+\-*/(). ]+$", t):
        return bot.reply_to(message, "Используйте только цифры и знаки + - * /")
     try:
            r = eval(t)
            bot.reply_to(message, f"{r}")
     except:
            bot.reply_to(message, "/")


@bot.message_handler(commands=['coin'])
def send_coin(message):
       c = coins()
       bot.reply_to(message, c)

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
