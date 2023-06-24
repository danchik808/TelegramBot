import telebot
bot = telebot.TeleBot('6258135076:AAFkroW8b6iAbyyb55pftP7JkFvzYL4T3NU')
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет! Давай перейдем к сайтам) 👋")
    markup.add(btn1)
    btn2 = types.KeyboardButton("Не люблю здороваться, давай переходить к делу 😡")
    markup.add(btn2)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помошник! 👋", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Привет! Давай перейдем к сайтам) 👋':
        markup = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Evklid', url="https://danchik808.github.io/Evklid/")
        btn8 = types.InlineKeyboardButton(text='Lagoona', url="https://danchik808.github.io/Lagoona/")
        btn9 = types.InlineKeyboardButton(text='NordSky', url="https://danchik808.github.io/NordSky/")
        btn10 = types.InlineKeyboardButton(text='NordSky2', url="https://danchik808.github.io/NordSky2/")
        btn11 = types.InlineKeyboardButton(text='PolitMC', url="https://danchik808.github.io/PolitMC/")
        btn12 = types.InlineKeyboardButton(text='FirstSkillboxHW', url="https://danchik808.github.io/FirstSkillboxHW")
        markup.add(btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.from_user.id, 'Какой сайт от Dan1x вам нужен? 😉', reply_markup=markup)

    elif message.text == 'Не люблю здороваться, давай переходить к делу 😡':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Ну ладно, прости пожалуйста)')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ой, какие мы не вежливые, извинись, а потом продолжим 😡', reply_markup=markup)

    elif message.text == 'Ну ладно, прости пожалуйста)':
        markup = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton(text='Evklid', url="https://danchik808.github.io/Evklid/")
        btn8 = types.InlineKeyboardButton(text='Lagoona', url="https://danchik808.github.io/Lagoona/")
        btn9 = types.InlineKeyboardButton(text='NordSky', url="https://danchik808.github.io/NordSky/")
        btn10 = types.InlineKeyboardButton(text='NordSky2', url="https://danchik808.github.io/NordSky2/")
        btn11 = types.InlineKeyboardButton(text='PolitMC', url="https://danchik808.github.io/PolitMC/")
        btn12 = types.InlineKeyboardButton(text='FirstSkillboxHW', url="https://danchik808.github.io/FirstSkillboxHW")
        markup.add(btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.from_user.id, 'Так уж и быть, прощаю) Какой сайт от Dan1x вам нужен? 😉', reply_markup=markup)

bot.polling(none_stop=True, interval=0)