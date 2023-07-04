from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import logging

load_dotenv('.env')

bot = Bot(token=os.environ.get('token'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


inline_buttons = [
    InlineKeyboardButton("Доллар США", callback_data='usd'),
    InlineKeyboardButton("Евро", callback_data='euro'),
    InlineKeyboardButton("Рубль", callback_data='rub'),
    InlineKeyboardButton("Казахстанский Тенге", callback_data='kzt'),
    InlineKeyboardButton("Информация о курсах валют", callback_data='info')
]
inline_keyboard = InlineKeyboardMarkup().add(*inline_buttons)


class UsdState(StatesGroup):
    usd = State()

class EuroState(StatesGroup):
    euro = State()

class RubState(StatesGroup):
    rub = State()

class KztState(StatesGroup):
    kzt = State()


@dp.callback_query_handler(lambda call: call)
async def all_inline(call):
    if call.data == 'usd':
        await usd(call.message)
    elif call.data == 'euro':
        await euro(call.message)
    elif call.data == 'rub':
        await rub(call.message)
    elif call.data == 'kzt':
        await kzt(call.message)
    elif call.data == 'info':
        await info(call.message)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}! Я помогу вам обменять деньги на нужную вам валюту или показать вам действительный курс обмена.",reply_markup=inline_keyboard)


@dp.message_handler(commands='info')
async def info(message: types.Message):
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    info_tag = soup.find_all('td', class_="exrate")
    await message.answer(f"1 USD={info_tag[1].get_text()} сом\n1 EUR={info_tag[3].get_text()} сом\n1 RUB={info_tag[5].get_text()} сом\n1 KZT={info_tag[7].get_text()} сом")


@dp.message_handler(commands='USD')
async def usd(message: types.Message):
    await message.answer(f"На какую сумму вы хотите совершить обмен")
    await UsdState.usd.set()

@dp.message_handler(state=UsdState.usd)
async def get_money(message: types.Message, state: FSMContext):
    await state.update_data(usd=message.text)
    data = await storage.get_data(user=message.from_user.id)
    amount = int(data['usd'])
    
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    info_tag = soup.find_all('td', class_="exrate")
    usd_money = info_tag[1].get_text()

    usd_rate_str = usd_money.replace(',', '.')
    usd_rate = float(usd_rate_str)

    converted_amount = amount * usd_rate
    await message.answer(f"За {amount} KGS вы получите примерно {converted_amount:.1f} USD.")


@dp.message_handler(commands='EURO')
async def euro(message: types.Message):
    await message.answer(f"На какую сумму вы хотите совершить обмен")
    await EuroState.euro.set()

@dp.message_handler(state=EuroState.euro)
async def get_money(message: types.Message, state: FSMContext):
    await state.update_data(euro=message.text)
    data = await storage.get_data(user=message.from_user.id)
    amount = int(data['euro'])

    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    info_tag = soup.find_all('td', class_="exrate")
    euro_money = info_tag[3].get_text()

    euro_rate_str = euro_money.replace(',', '.')
    euro_rate = float(euro_rate_str)

    converted_amount = amount * euro_rate
    await message.answer(f"За {amount} KGS вы получите примерно {converted_amount:.1f} EURO.")


@dp.message_handler(commands='RUB')
async def rub(message: types.Message):
    await message.answer(f"На какую сумму вы хотите совершить обмен")
    await RubState.rub.set()

@dp.message_handler(state=RubState.rub)
async def get_money(message: types.Message, state: FSMContext):
    await state.update_data(rub=message.text)
    data = await storage.get_data(user=message.from_user.id)
    amount = int(data['rub'])

    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    info_tag = soup.find_all('td', class_="exrate")
    rub_money = info_tag[5].get_text()

    rub_rate_str = rub_money.replace(',', '.')
    rub_rate = float(rub_rate_str)

    converted_amount = amount * rub_rate
    await message.answer(f"За {amount} KGS вы получите примерно {converted_amount:.1f} RUB.")
    


@dp.message_handler(commands='KZT')
async def kzt(message: types.Message):
    await message.answer(f"На какую сумму вы хотите совершить обмен")
    await KztState.kzt.set()


@dp.message_handler(state=KztState.kzt)
async def get_money(message: types.Message, state: FSMContext):
    await state.update_data(kzt=message.text)
    data = await storage.get_data(user=message.from_user.id)
    amount = int(data['kzt'])

    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    info_tag = soup.find_all('td', class_="exrate")
    kzt_money = info_tag[7].get_text()

    kzt_rate_str = kzt_money.replace(',', '.')
    kzt_rate = float(kzt_rate_str)

    converted_amount = amount * kzt_rate
    await message.answer(f"За {amount} KGS вы получите примерно {converted_amount:.1f} KZT.")

executor.start_polling(dp)
