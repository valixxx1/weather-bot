from pprint import pformat
import telebot
import requests
import json

with open('telebot.key', 'r') as f:
    tele_token = f.read()

with open('weather.key', 'r') as f:
    weather_key = f.read()

current_url = 'http://api.weatherapi.com/v1/current.json'

bot = telebot.TeleBot(tele_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    text = 'Welcome! This bot can tell you about weather. Just type /current'
    try:
        bot.send_message(message.chat.id, text)
    except:
        pass

@bot.message_handler(commands=['current'])
def current(message):
    query = {
        'key': weather_key,
        'q': message.text[len('/current '):]
    }

    response = requests.get(current_url, params=query)
    response.raise_for_status()
    response = json.loads(response.text)
    response = pformat(response)
    try:
        bot.reply_to(message, response)
    except:
        pass

bot.polling()