"Домашнее задние №3"
"Телеграмм-бот для онлайн магазина"
"Noglass Osh"

import asyncio

from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart, Command

from homework3.app.config1 import token

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.hendlers import router


bot=Bot(token=token)
dp=Dispatcher()

async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')