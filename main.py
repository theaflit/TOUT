import time

import telebot

from database import *
from insert_audio import *
from telebot import types
from config import Config
from summatization import summarization_text
from interact_yadisk import get_video, video_to_audio, get_all_files

token = Config.token_telegram
admin_id = Config.admin_id
bot = telebot.TeleBot(token)

dir_name = Config.dir_name

conn = get_db_connection()
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    send_question INTEGER
)
''')
conn.commit()
conn.close()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    add_user(message.chat.id)
    markup = menu_button()

    bot.send_message(message.chat.id,
                     "Добро пожаловать в ТОУТ! Не можете разобраться с домашкой или правильно распределить время? "
                     "Здесь вы сможете учиться легко и эффективно",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "create_note":
        bot.answer_callback_query(call.id, text="Жду ваш выбор...")
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton(text="Сократить текст 🖊", callback_data="start_create_note")
        btn2 = types.InlineKeyboardButton(text="Голосовое 🎙", callback_data="voice_note")
        btn4 = types.InlineKeyboardButton(text="Яндекс диск 💾", callback_data="ya_disk_note")

        markup.add(btn1, btn2)
        markup.add(btn4)
        bot.send_message(call.message.chat.id, "Выберете формат", reply_markup=markup)

    elif call.data == "start_create_note":
        create_notes(call.message)

    elif call.data == "ya_disk_note":
        ya_disk_create_notes(call.message)


@bot.message_handler()
def send_question(message):
    if len(message.text) > 50 and get_send_question(message.chat.id):
        markup = menu_button()

        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        summary = summarization_text(message.text)
        bot.send_message(message.chat.id, f"Вот ваш сокращенный текст:")
        bot.send_message(message.chat.id, f"{summary}", reply_markup=markup)

        set_send_question(message.chat.id, 0)


def create_notes(message):
    bot.send_message(message.chat.id, "Введите текст, который хотите сократить...")
    set_send_question(message.chat.id, 1)


def ya_disk_create_notes(message):
    """Функция для взаимодействия с яндекс диском и созданию конспекта по видео"""
    if message.chat.id == admin_id:
        markup = menu_button()
        all_files = get_all_files(dir_name)
        downloaded_files = get_video(dir_name, all_files)
        video_to_audio(downloaded_files)

        convert_to_wav("audio_files/file1.mp3")
        text = audio_to_text("audio_files/file1.wav")

        text = summarization_text(text)

        bot.send_message(message.chat.id, "Вот ваш сокращенный текст")
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Кажется у вас нет доступа к яндекс диску, подключенному к этому боту. Для "
                                          "доступа обратитесь к администратору @thealfit")


def menu_button():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="Создать конспект 📝", callback_data="create_note")
    btn3 = types.InlineKeyboardButton(text="Карточки 📁", callback_data="cards")
    btn4 = types.InlineKeyboardButton(text="Профиль 👤", callback_data="profile")

    markup.add(btn3, btn4)
    markup.add(btn1)
    return markup

bot.polling(none_stop=True)
#while True:
#    try:
#        # перезапуск бота при обнаружении ошибки
#        bot.polling(none_stop=True)
#    except Exception as e:
#        print(f"Ошибка: {e}. Перезапуск через 5 секунд...")
#        time.sleep(5)
