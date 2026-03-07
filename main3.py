import telebot
import random
import os
bot = telebot.TeleBot("")
image = (os.listdir(r"C:\Python Projects\password generator\.vscode\image"))
@bot.message_handler(commands=['Planeta'])
def send_samovar(message):
       with open(f"C:\Python Projects\password generator\.vscode\image\{image[0]}", "rb") as f:
              bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['Lesa'])
def send_lis(message):
    bot.reply_to(message, "Сегодня сорвал листик c дерева, a завтра:")
    with open(f"C:\Python Projects\password generator\.vscode\image\{image[1]}", "rb") as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['News'])
def send_stat(message):
      bot.reply_to(message, "https://plus-one.ru/manual/2021/08/31/15-krupneyshih-ekologicheskih-katastrof")     
      
@bot.message_handler(commands=["Soveti"])
def send_sovet(message):
      bot.reply_to(message, "Уже ничего не поможет, смирись") 

@bot.message_handler(commands=['Okeani'])
def send_s(message):
       with open(f"C:\Python Projects\password generator\.vscode\image\{image[2]}", "rb") as f:
              bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['Antarctida'])
def send_a(message):
    bot.reply_to(message, "Антаркида в 2027:")
    with open(f"C:\Python Projects\password generator\.vscode\image\{image[3]}", "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Есть команды: /Planeta, /Lesa, /News, /Soveti, /Okeani, /Antarctida")


bot.polling()
