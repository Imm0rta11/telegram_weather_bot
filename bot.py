import asyncio
import json
import requests
import keyboard
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

TOKEN = '6770092513:AAFe22IvTkh2PlDcwRzZZ27tryQdsu0GBNo'
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello i'm weather bot ", reply_markup=keyboard.main_kb)

@dp.message(Command(commands=['W', 'Weather']))
async def detect_weather(message: Message, command: CommandObject):
    try:
        city = command.args
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_key = 'f039fbd75b1dc47f381248ddae467482'
        res_pore = requests.get(base_url + 'appid=' + api_key + '&q=' + city).json()
        temp = str(round(res_pore['main']['temp'] - 273.15))
        weather = 'Weather:' + res_pore['weather'][0]['main']
        wind = 'Wind:' + str(res_pore['wind']['speed']) + 'km/h'
        visibility = res_pore['visibility'] / 1000
        country = res_pore['sys']['country']
        await message.answer(f'City: {city}\n Tempreture: {temp}\n Weather: {weather}\n Wind: {wind}\n Visibility: {visibility}\n Country: {country}')
    except KeyError:
        await message.answer('Please write current location!')

@dp.message()
async def show_credits(message: Message):
    msg = message.text.lower()
    if msg == 'credits':
        await message.answer('Credits: By Imm0rta11 Github', reply_markup=keyboard.cred_kb)
    elif msg == 'find out the weather':
        await message.answer('To find out what the weather is, you need to enter the command, here is the format of its writing /W location name')

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

