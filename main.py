import telebot
import requests
import json
import io

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

    image_url = 'http:' + response['current']['condition']['icon']
    image = requests.get(image_url)
    image = io.BytesIO(image.content)

    response = f'{response['current']['temp_c']} °C\n{response['current']['condition']['text']}'

    try:
        bot.send_photo(message.chat.id, image, caption=response)
    except:
        pass

bot.polling()