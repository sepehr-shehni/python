from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context= True)

def start(update,context):
    context.bot.sendChatAction(update.message.chat_id,"typing")
    context.bot.send_message(text='سلام به ربات تک وان 24 خوش اومدی . \n برای اطلاعات بیشتر روی دستور /help   کلیک نمایید',chat_id=update.message.chat_id)

def send_location(update,context):
    chat_id = update.message.chat_id
    context.bot.sendLocation(chat_id,'37.213975', '50.001957')


token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('location',send_location))

token.start_polling()
token.idle()






token.dispatcher.add_handler(CommandHandler('start',start))


token.start_polling()
token.idle()

