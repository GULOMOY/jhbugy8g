from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update

def start(update:Update, context:CallbackContext):
    update.message.reply_text("Assalom alaykum")

if name=='main':
    updater = Updater(token='2084065750:AAFmMnvZiukuPpzs4UMpZwLGAF8OxtQLX0c',use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()