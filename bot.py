from crypto_tracker import get_prices
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from crypto_tracker import get_prices

telegram_token = 'Telegram API Key'

updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.3f}\nDay Change: {change_day:.3f}%\nHour Change: {change_hour:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
