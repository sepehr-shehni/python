from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context= True)

def start(update,context):
    context.bot.send_message(text='سلام به ربات تک وان 24 خوش اومدی . \n برای اطلاعات بیشتر روی دستور /help   کلیک نمایید',chat_id=update.message.chat_id)


def send_document(update,context):
    chat_id = update.message.chat_id
    document = open('E:\\Project\\Python Project\\Robot\\Telegram\\python.pdf','rb')
    context.bot.sendDocument(chat_id,document)

token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('document',send_document))

token.start_polling()
token.idle()

