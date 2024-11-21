import telebot

bot = telebot.TeleBot('7856907656:AAGnUV0HwKa3rK-xsX8uEAQAzHiZP7b97u4')


@bot.message_handlers(commands=['start'])
def nain(messadge):
    bot.send_messadge(messadge.chat.id, 'Привет')
