from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
from telegram import ReplyKeyboardMarkup


token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context=True)

def start(update , context):
    key = [['وبسایت تک وان 24'] , ['کانال تک وان 24' , 'اینستاگرام تک وان 24']]
    key_2 = ReplyKeyboardMarkup(key)
    context.bot.send_message(chat_id= update.message.chat_id , text='سلام به ربات تک وان 24 خوش اومدید.' , reply_markup=key_2)
def techone24_info(update , context):
    if update.message.text == 'وبسایت تک وان 24':
        context.bot.send_message(chat_id= update.message.chat_id , text= 'https://techone24.com')
    elif update.message.text == 'کانال تک وان 24':
        context.bot.send_message(chat_id= update.message.chat_id , text= '@techone24')
    elif update.message.text == 'اینستاگرام تک وان 24':
        context.bot.send_message(chat_id= update.message.chat_id , text = 'https://www.instagram.com/techone24/')


token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(MessageHandler(Filters.text , techone24_info))

token.start_polling()
token.idle()