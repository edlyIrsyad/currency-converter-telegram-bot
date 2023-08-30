from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from forex_python.converter import CurrencyRates

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def start(update, context):
    update.message.reply_text("Welcome to the Currency Converter Bot! Use /convert to convert currencies.")

def convert(update, context):
    try:
        args = context.args
        if len(args) != 3:
            update.message.reply_text("Usage: /convert <amount> <from_currency> <to_currency>")
            return

        amount = float(args[0])
        from_currency = args[1].upper()
        to_currency = args[2].upper()

        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)

        update.message.reply_text(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}")
    except Exception as e:
        update.message.reply_text("An error occurred. Please check your input and try again.")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("convert", convert))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
