import telebot
import requests
from typing import Any, Dict, List

bot = telebot.TeleBot("6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk")
users: List[int] = []
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "- Assalom aleykum -\nMarhamat⁉\nKasb-hunar maktabi haqida🏫\n/KHM\nDars jadvali↙️\n/dars 📚\nAriza yuborish uchun↙️\n/ariza 📑\nYaratuvchilar:↙️\n/admins")
    if not(message.chat.id in users):
        user_first_name = str(message.chat.first_name)
        user_username = str(message.chat.username)
        users.append(message.chat.id)
        users.append(user_first_name)
        users.append(f'@{user_username}')
        tt=f'Yangi foydalanuvchi👀✅\n👤{user_first_name}\n-User:@{user_username}'
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text={tt}', auth=('user', 'pass'))

@bot.message_handler(commands=['botinfo'])
def ib_m(message):
    bot.send_message(message.chat.id, f"Bo'tdan foydalanganlar soni-{int(len(users)/3)}ta \nChat_id va Usernamelar: {users}")

@bot.message_handler(commands=['ariza'])
def send_ariza(message):
        bot.reply_to(message, "- Marhamat arizangizni to'ldiring -\nNamuna:📄 ⬇\n• 1-F.I.Sh : \n• 2-Telefon raqam: \n• 3-Yashash joyingiz:\n• 4-Arizangizni kiriting:\n• 5-Sana/vaqt:\nMisol uchun🎥⏬")
        bot.send_video(message.chat.id, video=open('ariza_bot_vd.mp4', 'rb'), supports_streaming=True)
@bot.message_handler(commands=['admins'])
def b_ad(message):
        bot.send_message(message.chat.id,'@umidabduvahobov\n@ismoilbahtiyorov')
@bot.message_handler(commands=['dars'])
def send_ariza(message):
        bot.send_message(message.chat.id, "Guruhni tanlang🤷👬\n1-bosqich 🐺🐺🐺\n/1_23 🚘🛠\n/2_23 💻📟\n/3_23 💻📡\n/4_23 🖥🎑\n/5_23 ⚖️💰\n/6_23 🎇🗜\n/7_23 🎀✂️\n2-bosqich 🦁🦁🦁\n/1_22 🚙⚙\n/2_22 🏎🪄\n/3_22 🖥🖨\n/4_22 🖥🖨\n/5_22 💽🌄\n/6_22 💽🌄\n/7_22 🗜🪄\n/8_22 🎁✂️")

@bot.message_handler(commands=['KHM'])
def send_ariza(message):
        bot.send_message(message.chat.id, "https://t.me/kasb_hunar_maktabi_2son")

@bot.message_handler(commands=['1_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"1-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n1.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['2_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"2-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n2.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['3_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"3-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n3.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['4_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"4-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n4.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['5_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"5-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n5.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['6_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"6-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n6.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['7_23'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"7-23.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n7.23-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['1_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"1-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n1.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['2_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"2-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n2.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['3_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"3-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n3.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['4_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"4-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n4.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['5_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"5-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n5.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['6_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"6-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n6.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['7_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"7-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n7.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))

@bot.message_handler(commands=['8_22'])
def msg4(message):
        bot.send_photo(message.chat.id, photo = open(r"8-22.png", 'rb'))
        user_first_name2 = str(message.chat.first_name)
        user_username2 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Dars jadvali olindi📚✅\n8.22-guruh\nName:{user_first_name2}\nUsername:@{user_username2}', auth=('user', 'pass'))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    #bot.reply_to(message, message.text)
    #print(message.text)
    text_a=message.text
    #print(len(text_a))
    if len(text_a)>100:
        user_first_name1 = str(message.chat.first_name)
        user_username1 = str(message.chat.username)
        requests.get(f'https://api.telegram.org/bot6510996618:AAGXGMt_ynBYuP20KD5W5hVrgLnnuxT9GHk/sendMessage?chat_id=@ikkinchisonkhmariza&text=Ariza qabul qilindi✅\n{text_a}\nName:{user_first_name1}\nUsername:@{user_username1}', auth=('user', 'pass'))
        bot.reply_to(message, "Arizangiz qabul qilindi.\nTez orada Chinoz tuman 2-son kasb-hunar maktabi mamuriyati siz bilan bog'lanadi.\nEtiboringiz uchun rahmat✅")
        bot.send_message(message.chat.id, "- Assalom aleykum -\nMarhamat⁉\nKasb-hunar maktabi haqida🏫\n/KHM\nDars jadvali↙️\n/dars 📚\nAriza yuborish uchun↙️\n/ariza 📑")
    else:
        bot.reply_to(message, "Noto'g'ri malumot❌")
bot.infinity_polling()
