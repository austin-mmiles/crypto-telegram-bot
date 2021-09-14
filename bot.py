import telebot
import time

bot_token = '1975828844:AAGLPaGuzPbpKfuZteAUcyD9y9rGZUPm920'
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, Welcome!")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "To use this bot, send a username")


bot.polling()
