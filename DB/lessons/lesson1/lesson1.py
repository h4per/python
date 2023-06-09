from aiogram import Bot, Dispatcher, types, executor
from config import token
import random


bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу помочь?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.reply("Здарова")

@dp.message_handler(commands='game')
async def guess_num(message:types.Message):
    await message.reply("Я загадал число от 1 до 3 угадайте")

@dp.message_handler()
async def num(message:types.Message):
    guess = int(message.text)
    secret_number = random.randint(1, 3)
    if guess == secret_number:
        await message.reply("Правильно,вы отгадали!!!")
    else:
        await message.reply("Блииин,попробуйте еще раз")

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)