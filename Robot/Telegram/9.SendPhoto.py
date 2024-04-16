from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context= True)

def start(update,context):
    context.bot.send_message(text='سلام به ربات تک وان 24 خوش اومدی . \n برای اطلاعات بیشتر روی دستور /Send-Photo   کلیک نمایید',chat_id=update.message.chat_id)


def send_Photo(update,context):
    photo = open('E:\\Project\\Python Project\\Robot\\Telegram\\hacker.jpg' , 'rb')
    context.bot.sendPhoto(update.message.chat_id,photo)

token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('photo',send_Photo))

token.start_polling()
token.idle()

