from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context=True)

def start(update , context):
    key = [[InlineKeyboardButton('وبسایت تک وان 24' , callback_data='1')] , [InlineKeyboardButton('کانال تک وان 24' , callback_data='2')]]
    key_2 = InlineKeyboardMarkup(key)
    context.bot.send_message(chat_id= update.message.chat_id , text='سلام به ربات تک وان 24 اومدید.')
    context.bot.send_message(chat_id= update.message.chat_id , text= 'دکمه مورد نظر خود را انتخاب نمایید',reply_markup=key_2)
def techone24_info(update , context):
    query = update.callback_query
    if (query.data == '1'):
        context.bot.send_message(chat_id=query.message.chat_id , text='https://techone24.com')
    if query.data == '2':
        context.bot.send_message(chat_id= query.message.chat_id , text= "@techone24")
token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(CallbackQueryHandler(techone24_info))

token.start_polling()
token.idle()