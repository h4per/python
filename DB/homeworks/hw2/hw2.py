from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token
import logging

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

keyboard_buttons = [
    KeyboardButton('/start'),
    KeyboardButton('/help'),
    KeyboardButton('/backend'),
    KeyboardButton('/frontend'),
    KeyboardButton('/uxui'),
    KeyboardButton('/android'),
    KeyboardButton('/ios')

]
keyboard_one = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=30).add(*keyboard_buttons)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.",  reply_markup=keyboard_one)

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу помочь?")

@dp.message_handler(commands='backend')
async def backend(message:types.Message):
    await message.answer("Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. Для ее разработки могут использоваться самые разные языки, например, Python, PHP, Go, JavaScript, Java, С#.\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев.")

@dp.message_handler(commands='frontend')
async def frontend(message:types.Message):
    await message.answer("Frontend — презентационная часть информационной или программной системы, её пользовательский интерфейс и связанные с ним компоненты.\nСтоимость курса: 10000 сом в месяц.\nОбучение: 5 месяцев.")

@dp.message_handler(commands='uxui')
async def uxui(message:types.Message):
    await message.answer("UX/UI-дизайн — это проектирование удобных, понятных и эстетичных пользовательских интерфейсов.\nСтоимость курса: 8000 сом в месяц.\nОбучение: 4 месяцев")

@dp.message_handler(commands='android')
async def android(message:types.Message):
    await message.answer("Android Developer - создает мобильные приложения на операционной системе Android. Андроид-программист использует языки Java, Kotlin, C++,  иногда Javascript.\nСтоимость курса: 12000 сом в месяц\nОбучение: 14 месяцев")

@dp.message_handler(commands='ios')
async def ios(message:types.Message):
    await message.answer("IOS Developer - создает мобильные приложения на операционной системе IOS. IOS-программист использует язык Swift.\nСтоимость курса: 10000 сом в месяц.\nОбучение: 12 месяцев.")

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)
