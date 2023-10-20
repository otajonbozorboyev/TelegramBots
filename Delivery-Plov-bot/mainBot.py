# Commercial Bot - Samosh-Bot

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import TOKEN
import sections

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    name = update.message.from_user.full_name
    update.message.reply_text(get_text('start').format(name=name),reply_markup = sections.main_section)

def products(update: Update, context: CallbackContext):
    update.message.reply_text(get_text('choose'), reply_markup = sections.product_section)

def main():
    """Start the Bot"""

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text("Asosiyga qaytish"), start))
    dispatcher.add_handler(MessageHandler(Filters.text("🛍 Buyurtma berish"), products))
    dispatcher.add
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




