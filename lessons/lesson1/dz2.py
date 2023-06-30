from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pytube import YouTube
import os, logging, smtplib, sqlite3, time, requests


load_dotenv('.env')

bot = Bot(os.environ.get('token'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

database = sqlite3.connect('smtp2.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(200),
    created VARCHAR(200)
);
""")
cursor.connection.commit()


inline_buttons = [
    InlineKeyboardButton('Отправить сообщение', callback_data='send_button'),
    InlineKeyboardButton('Отправить MP4 файл(видео)', callback_data='send_video'),
    InlineKeyboardButton('Отправить MP3 файл(аудио)', callback_data='send_audio')
]
inline_keyboard = InlineKeyboardMarkup().add(*inline_buttons)


@dp.callback_query_handler(lambda call: call)
async def inline(call):
    if call.data == 'send_button':
        await send_command(call.message)
    elif call.data == 'send_video':
        await send_command2(call.message)
    elif call.data == 'send_audio':
        await send_command3(call.message)


class EmailState(StatesGroup):
    to_email = State()
    subject = State()
    message = State()


@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id};")
    result = cursor.fetchall()
    if result == []:
        cursor.execute(f"""INSERT INTO users (user_id, username, first_name,
                    last_name, created) VALUES ({message.from_user.id},
                    '{message.from_user.username}',
                    '{message.from_user.first_name}', 
                    '{message.from_user.last_name}',
                    '{time.ctime()}');
                    """)
    cursor.connection.commit()
    await message.answer(f'Здравствуй,{message.from_user.full_name}! Я помогу тебе отправлять сообщения, видео или аудио на почту кому угодно.', reply_markup=inline_keyboard)


@dp.message_handler(commands='send')
async def send_command(message:types.Message):
    await message.answer('Введите почту на которую нужно отправить сообщение:')
    await EmailState.to_email.set()


@dp.message_handler(state=EmailState.to_email)
async def get_subject(message:types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()

    cursor.execute("""UPDATE users SET email=? WHERE user_id=?""", (data['email'], message.from_user.id))
    cursor.connection.commit()

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

    msg['Subject'] = res['subject']
    msg['From'] = os.environ.get('smtp_email')
    msg['To'] = res['email']

    try:
        server.login(sender, password)
        server.send_message(msg)
        await message.answer('Ваше сообщение успешно отправлено!')
    except Exception as error:
        await message.answer(f'Произошла ошибка попробуйте еще раз.\n{error}')

    await state.finish()


class VideoState(StatesGroup):
    url = State()
    to_email = State()
    subject = State()
    video = State()


@dp.message_handler(commands='video')
async def send_command2(message:types.Message):
    await message.answer('Введите почту на которую нужно отправить видео файл:')
    await VideoState.to_email.set()


@dp.message_handler(state=VideoState.to_email)
async def get_subject(message:types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите заголовок:')
    await VideoState.subject.set()


@dp.message_handler(state=VideoState.subject)
async def get_url(message:types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer('Отправьте ссылку...')
    await VideoState.url.set()


@dp.message_handler(state=VideoState.url)
async def get_video(message:types.Message):
    yt = YouTube(message.text, use_oauth=True)
    await message.answer("Скачиваем видео...")
    try:
        yt.streams.filter(file_extension='mp4').first().download('video', f'{yt.title}.mp4')
        await message.answer("Скачалось, отправляю...")
        with open(f'video/{yt.title}.mp4', 'rb') as video:
            await bot.send_video(message.chat.id, video)
            await AudioState.video.set()
            await message.answer('Перешлите мне этот файл чтобы я смог отправить его на почту')
            
    except:
        yt.streams.filter(file_extension='mp4').first().download('video', f'{yt.author}.mp4')
        await message.answer("Скачалось, отправляю...")
        with open(f'video/{yt.author}.mp4', 'rb') as video:
            await bot.send_video(message.chat.id, video)
            await VideoState.video.set()
            await message.answer('Перешлите мне этот файл чтобы я смог отправить его на почту')


@dp.message_handler(content_types=types.ContentType.VIDEO, state=VideoState.video)
async def send_video(message: types.Message, state: FSMContext):
    await state.update_data(video=message.video.file_id)
    await message.answer('Отправляем видео файл...')
    res = await storage.get_data(user=message.from_user.id)

    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_email_password')
    video_file_id = res['video']

    video_file = await bot.get_file(video_file_id)
    video_path = video_file.file_path

    video_url = f"https://api.telegram.org/file/bot{os.environ.get('token')}/{video_path}"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = MIMEMultipart()
    msg['Subject'] = res['subject']
    msg['From'] = os.environ.get('smtp_email')
    msg['To'] = res['email']

    part = MIMEBase('video', 'mp4')
    part.set_payload(requests.get(video_url).content)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="video.mp4")
    msg.attach(part)

    try:
        server.login(sender, password)
        server.send_message(msg)
        await message.answer('Ваше сообщение успешно отправлено!')
    except Exception as error:
        await message.answer(f'Произошла ошибка. Попробуйте еще раз.\n{error}')

    await state.finish()


class AudioState(StatesGroup):
    url = State()
    to_email = State()
    subject = State()
    audio = State()


@dp.message_handler(commands='audio')
async def send_command3(message:types.Message):
    await message.answer('Введите почту на которую нужно отправить аудио файл:')
    await AudioState.to_email.set()


@dp.message_handler(state=AudioState.to_email)
async def get_subject(message:types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите заголовок:')
    await AudioState.subject.set()


@dp.message_handler(state=AudioState.subject)
async def get_url(message:types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer('Отправьте ссылку...')
    await AudioState.url.set()


@dp.message_handler(state=AudioState.url)
async def download_audio(message: types.Message):
    yt = YouTube(message.text, use_oauth=True)
    await message.answer("Скачиваем аудио, ожидайте...")
    try:
        yt.streams.filter(only_audio=True).first().download('audio', f'{yt.title}.mp3')
        await message.answer("Скачалось, отправляю...")
        with open(f'audio/{yt.title}.mp3', 'rb') as audio:
            await bot.send_audio(message.chat.id, audio)
            await AudioState.audio.set()
            await message.answer('Перешлите мне этот файл чтобы я смог отправить его на почту')

    except:
        yt.streams.filter(only_audio=True).first().download('audio', f'{yt.author}.mp3')
        await message.answer("Скачалось, отправляю...")
        with open(f'audio/{yt.author}.mp3', 'rb') as audio:
            await bot.send_audio(message.chat.id, audio)
            await AudioState.audio.set()
            await message.answer('Перешлите мне этот файл чтобы я смог отправить его на почту')


@dp.message_handler(content_types=types.ContentType.AUDIO, state=AudioState.audio)
async def send_audio(message: types.Message, state: FSMContext):
    await state.update_data(audio=message.audio.file_id)
    await message.answer('Отправляем аудио файл...')
    res = await storage.get_data(user=message.from_user.id)

    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_email_password')
    audio_file_id = res['audio']

    audio_file = await bot.get_file(audio_file_id)
    audio_path = audio_file.file_path

    audio_url = f"https://api.telegram.org/file/bot{os.environ.get('token')}/{audio_path}"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = MIMEMultipart()
    msg['Subject'] = res['subject']
    msg['From'] = os.environ.get('smtp_email')
    msg['To'] = res['email']

    part = MIMEBase('audio', 'mpeg3')
    part.set_payload(requests.get(audio_url).content)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="audio.mp3")
    msg.attach(part)

    try:
        server.login(sender, password)
        server.send_message(msg)
        await message.answer('Ваше сообщение успешно отправлено!')
    except Exception as error:
        await message.answer(f'Произошла ошибка. Попробуйте еще раз.\n{error}')

    await state.finish()

executor.start_polling(dp)