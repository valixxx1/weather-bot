import telebot

with open('telebot.key', 'r') as f:
    token = f.read()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    text = "Welcome! This bot can tell you about weather."
    bot.send_message(message.chat.id, text)

bot.polling()