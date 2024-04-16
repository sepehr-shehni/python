from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I',use_context=True)

def start(update,context):
    context.bot.send_message(text='سلام به ربات ارژنگ خوش اومدی . \n برای اطلاعات بیشتر روی دستور /help   کلیک نمایید',chat_id=update.message.chat_id)

def website(update,context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'وبسایت ما : n\ https://arjang.ac.ir')
def help (update,context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'برای دریافت ادرس وب سایت ما از دستور /website  استفاده کنید \n برای شروع مجدد ربات از /start  استفاده نمایید.')

token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('website',website))
token.dispatcher.add_handler(CommandHandler('help' , help))

token.start_polling()
token.idle()
