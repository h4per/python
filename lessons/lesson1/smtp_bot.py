from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os, logging, smtplib, sqlite3, time, random


load_dotenv('.env')

bot = Bot(os.environ.get('token'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

database = sqlite3.connect('smtp.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    chat_id INT,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    verified BOOLEAN,
    phone VARCHAR(200),
    email VARCHAR(200),
    created VARCHAR(100)
);
""")
cursor.connection.commit()


class EmailState(StatesGroup):
    to_email = State()
    subject = State()
    message = State()


inline_buttons = [
    InlineKeyboardButton('Отправить сообщение', callback_data='send_button')
]
inline_keyboard = InlineKeyboardMarkup().add(*inline_buttons)


@dp.callback_query_handler(lambda call: call)
async def all_inline(call):
    if call.data == 'send_button':
        await send_command(call.message)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id};")
    result = cursor.fetchall()
    if result == []:
        cursor.execute(f"""INSERT INTO users (user_id, chat_id, username, first_name,
                    last_name, verified, created) VALUES ({message.from_user.id},
                    {message.chat.id}, '{message.from_user.username}',
                    '{message.from_user.first_name}', 
                    '{message.from_user.last_name}',
                    False,
                    '{time.ctime()}');
                    """)
    cursor.connection.commit()
    await message.answer(f'Здравствуй,{message.from_user.full_name}! Я помогу тебе отправлять сообщения на почту кому угодно.\nНапиши:  /send', reply_markup=inline_keyboard)


@dp.message_handler(commands='send')
async def send_command(message:types.Message):
    await message.answer('Введите почту на которую нужно отправить сообщение:')
    await EmailState.to_email.set()


@dp.message_handler(state=EmailState.to_email)
async def get_subject(message:types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите заголовок:')
    await EmailState.subject.set()


@dp.message_handler(state=EmailState.subject)
async def get_message(message:types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer('Введите сообщение:')
    await EmailState.message.set()


@dp.message_handler(state=EmailState.message)
async def send_message(message:types.Message, state: FSMContext):
    await state.update_data(message=message.text)
    await message.answer('Отправляем сообщение...')
    res = await storage.get_data(user=message.from_user.id)

    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_email_password')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = EmailMessage()
    msg.set_content(res['message'])

    msg = MIMEMultipart()
    msg['Subject'] = res['subject']
    msg['From'] = os.environ.get('smtp_email')
    msg['To'] = res['email']

    video_path = 'urapobeda.mp4'
    video_filename = os.path.basename(video_path)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(video_path, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{video_filename}"')
    msg.attach(part)

    try:
        server.login(sender, password)
        server.send_message(msg)
        await message.answer('Ваше сообщение успешно отправлено!')
    except Exception as error:
        await message.answer(f'Произошла ошибка попробуйте еще раз.\n{error}')

    await state.finish()


class VerifyState(StatesGroup):
    email = State()
    random_code = State()
    code = State()


@dp.message_handler(commands='verify')
async def get_verify_code(message:types.Message):
    await message.answer('Введите почту для верификации:')
    await VerifyState.email.set()


@dp.message_handler(state=VerifyState.email)
async def send_verify_code(message:types.Message, state:FSMContext):
    await message.answer('Отправляем код верификации...')
    random_code = random.randint(111111,999999)
    await state.update_data(email=message.text)
    await state.update_data(random_code=random_code)
    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_email_password')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = EmailMessage()
    msg.set_content(f'Здравствуйте,ваш код: {random_code}')

    msg['Subject'] = 'Код верификации'
    msg['From'] = os.environ.get('smtp_email')
    msg['To'] = message.text

    try:
        server.login(sender, password)
        server.send_message(msg)
        await message.answer('Ваше сообщение успешно отправлено!')
    except Exception as error:
        await message.answer(f'Произошла ошибка попробуйте еще раз.\n{error}')

    await message.answer('Введите код верификации:')
    await VerifyState.code.set()


@dp.message_handler(state=VerifyState.code)
async def check_verify_code(message:types.Message, state:FSMContext):
    await message.reply('Начинаю проверку кода...')
    result = await storage.get_data(user=message.from_user.id)
    print(result)
    if result['random_code'] == int(message.text):
        await message.answer('Код совпал, проходите дальше.')
        user_email = result['email']
        cursor.execute(f"UPDATE users SET email = '{user_email}', verified = True WHERE user_id = {message.from_user.id};")
        cursor.connection.commit()
    else:
        await message.answer('Неправильный код.')
        
executor.start_polling(dp)