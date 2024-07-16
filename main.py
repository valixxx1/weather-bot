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

def emoji_by_weather(code):
    if code == 1000:
        return '☀️'
    elif code == 1003:
        return '🌤'
    elif code == 1006:
        return '☁️'
    elif code == 1009:
        return '☁️'
    elif code == 1030:
        return '🌫'
    elif code == 1063:
        return '🌧'
    elif code == 1066:
        return '🌨'
    elif code == 1069:
        return '🌨'
    elif code == 1072:
        return '🌨'
    elif code == 1087:
        return '🌩'
    elif code == 1114:
        return '🌨'
    elif code == 1117:
        return '🌨'
    elif code == 1135:
        return '🌫'
    elif code == 1147:
        return '🌫'
    elif code == 1150:
        return '🌦'
    elif code == 1153:
        return '🌦'
    elif code == 1168:
        return '🌨'
    elif code == 1171:
        return '🌨'
    elif code == 1180:
        return '🌧'
    elif code == 1183:
        return '🌧'
    elif code == 1186:
        return '🌦'
    elif code == 1189:
        return '🌧'
    elif code == 1192:
        return '🌧'
    elif code == 1195:
        return '🌧'
    elif code == 1198:
        return '🌨'
    elif code == 1201:
        return '🌨'
    elif code == 1204:
        return '🌨'
    elif code == 1207:
        return '🌨'
    elif code == 1210:
        return '🌨'
    elif code == 1213:
        return '🌨'
    elif code == 1216:
        return '🌨'
    elif code == 1219:
        return '🌨'
    elif code == 1222:
        return '🌨'
    elif code == 1225:
        return '🌨'
    elif code == 1237:
        return '🌨'
    elif code == 1240:
        return '🌧'
    elif code == 1243:
        return '🌧'
    elif code == 1246:
        return '🌧'
    elif code == 1249:
        return '🌨'
    elif code == 1252:
        return '🌨'
    elif code == 1255:
        return '🌨'
    elif code == 1258:
        return '🌨'
    elif code == 1261:
        return '🌨'
    elif code == 1264:
        return '🌨'
    elif code == 1273:
        return '⛈'
    elif code == 1276:
        return '⛈'
    elif code == 1279:
        return '⛈'
    elif code == 1282:
        return '⛈'
    else:
        return ''

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

    response = f'{emoji_by_weather(response['current']['condition']['code'])}\n{response['current']['temp_c']} °C\n{response['current']['condition']['text']}'

    try:
        bot.send_message(message.chat.id, response)
    except:
        pass

bot.polling()