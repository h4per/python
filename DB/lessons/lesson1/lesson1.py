# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# import sqlite3, time,logging
# import random

# bot = Bot(token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)


# database = sqlite3.connect('users.db')
# cursor = database.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS users(
#     user_id INT,
#     chat_id INT,
#     username VARCHAR(255),
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     created VARCHAR(100)
# );
# """)
# cursor.connection.commit()

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer(f"Привет, {message.from_user.full_name}!")
#     cursor.execute(f"SELECT  * FROM users WHERE user_id = {message.from_user.id}")
#     result = cursor.fetchall()
#     if result == []:
#         cursor.execute(f"""INSERT INTO users VALUES ({message.from_user.id},
#                     {message.chat.id}, '{message.from_user.username}',
#                     '{message.from_user.first_name}', 
#                     '{message.from_user.last_name}',
#                     '{time.ctime()}');
#                     """)
#     cursor.connection.commit()

# @dp.message_handler(commands='help')
# async def help(message:types.Message):
#     await message.answer("Чем могу помочь?")

# @dp.message_handler(commands='mailing')
# async def mailing(message:types.Message):
#     await message.reply("Введите текст для рассылки: ")

# @dp.message_handler(commands='game')
# async def guess_num(message:types.Message):
#     await message.reply("Я загадал число от 1 до 3 угадайте")

# @dp.message_handler()
# async def num(message:types.Message):
#     guess = int(message.text)
#     secret_number = random.randint(1, 3)
#     if guess == secret_number:
#         await message.reply("Правильно,вы отгадали!!!")
#     else:
#         await message.reply("Блииин,попробуйте еще раз")

# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("Я вас не понял, введите /help")

# executor.start_polling(dp)

# файл с дз 1 и уроком 1,2

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token
import sqlite3, time, logging

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

database = sqlite3.connect('users.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    chat_id INT,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created VARCHAR(100)
);
""")
cursor.connection.commit()

keyboard_buttons = [
    KeyboardButton('/start'),
    KeyboardButton('/mailing'),
    KeyboardButton('/help'),
]
keyboard_one = ReplyKeyboardMarkup(resize_keyboard=True).add(*keyboard_buttons)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id};")
    result = cursor.fetchall()
    if result == []:
        cursor.execute(f"""INSERT INTO users VALUES ({message.from_user.id},
                    {message.chat.id}, '{message.from_user.username}',
                    '{message.from_user.first_name}', 
                    '{message.from_user.last_name}',
                    '{time.ctime()}');
                    """)
    cursor.connection.commit()
    await message.answer(f"Привет,{message.from_user.full_name}!", reply_markup= keyboard_one)

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем я могу вам помочь?")

@dp.message_handler(text="Привет")
async def hello(message:types.Message):
    await message.reply("Здарова")

class MailingState(StatesGroup):
    text = State()

@dp.message_handler(commands='mailing')
async def mailing(message:types.Message):
    if message.from_user.id in [1460696649]:
        await message.reply("Введите текст для рассылки:")
        await MailingState.text.set()
    else:
        await message.answer("У вас нет прав")

@dp.message_handler(state=MailingState.text)
async def send_mailing_text(message:types.Message, state:FSMContext):
    await message.answer("Начинаю рассылку...")
    cursor.execute("SELECT chat_id FROM users;")
    chats_id = cursor.fetchall()
    for chat in chats_id:
        await bot.send_message(chat[0], message.text)
    await message.answer("Рассылка окончена.")
    await state.finish()

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)