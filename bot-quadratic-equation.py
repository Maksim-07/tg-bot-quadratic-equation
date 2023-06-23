import os
from dotenv import load_dotenv
from class_discriminant import Discriminant

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command, Text

load_dotenv()
TOKEN = os.getenv('TOKEN_BOT')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(Command('start'))
async def command_start(message: types.Message):
    chat_id = message.from_id
    name = message.from_user.first_name
    await message.reply(f"Привет, {name}.\n"
                        f"Помогу решить квадратное уравнение вида: ax^2+bx+c=0,  (a ≠ 0)\n"
                        f"Введи 3 числа через пробел.")


@dp.message_handler()
async def discriminant(message: types.Message):
    chat_id = message.from_id
    number = message.text.split(' ')
    try:
        disc = Discriminant(int(number[0]), int(number[1]), int(number[2]))
        await bot.send_message(chat_id, str(disc))
    except (ValueError, IndexError):
        await message.reply('Введите числа через пробел!')


if __name__ == '__main__':
    executor.start_polling(dp)
