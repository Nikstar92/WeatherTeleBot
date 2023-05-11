import telebot
import requests
import json

bot = telebot.TeleBot('6263478357:AAEjFZN2nXCLxk4LUfr_EZX_GIlKAJ_cI5k')
API = 'e7ac9efc14b0e05bba39d2ca34c39e96'


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name} {message.from_user.last_name}. Напиши название города.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data['weather'][0]['description']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        bot.reply_to(message, f'Сейчас погода в городе {city} - {temp:.1f} °C, ощущается как - {feels_like:.1f}°C,'
                              f' на улице - {weather}, атмосферное давление - {pressure} мм рт.ст.,'
                              f' влажность воздуха - {humidity} %, скорость ветра - {wind:.1f} м/с.')

        # bot.reply_to(message, f'Сейчас погода в городе {city} - {data}')
        # match weather:
        #     case 'ясно': image = 'clear sky.png'
        #     case 'drizzle': image = 'drizzle.png'
        #     case 'переменная облачность': image = 'few clouds.png'
        #     case 'mist': image = 'mist.png'
        #     case 'overcast clouds': image = 'overcast clouds.png'
        #     case 'rain': image = 'rain.png'
        #     case 'shower rain': image = 'shower rain.png'
        #     case 'snow': image = 'snow.png'
        #     case 'thunderstorm': image = 'thunderstorm.png'
        # if weather == 'clear sky':
        #     image = 'clear sky.png'
        # elif weather == 'drizzle':
        #     image = 'drizzle.png'
        # elif weather == 'few clouds':
        #     image = 'few clouds.png'
        # elif weather == 'mist':
        #     image = 'mist.png'
        # elif weather == 'broken clouds':
        #     image = 'overcast clouds.png'
        # elif weather == 'rain':
        #     image = 'rain.png'
        # elif weather == 'shower rain':
        #     image = 'shower rain.png'
        # elif weather == 'snow':
        #     image = 'snow.png'
        # else:
        #     image = 'thunderstorm.png'
        # file = open('./' + image, 'rb')
        # bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно')


bot.polling(none_stop=True)
