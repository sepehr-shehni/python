from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context=True)

def start1(update , context):
    context.bot.send_message(text='سلام {} به ربات ارژنگ خوش امدید . \n برای اطلاعات بیشتر روی دستور /help   کلیک نماییید.'.format(update.message.from_user.first_name),chat_id=update.message.chat_id)
    context.bot.send_message(chat_id= update.message.chat_id , text= 'id : {} \n user : {} \n firstname : {}'.format(update.message.chat_id , update.message.from_user.username ,update.message.from_user.first_name ))
    print(update.message)
def website(update , context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'وبسایت ما :n\ https://arjang.ac.ir')
def help1 (update , context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'برای دریافت ادرس وب سایت ما از دستور /website  استفاده کنید \n برای شروع مجدد ربات از /start  استفاده نمایید.')

token.dispatcher.add_handler(CommandHandler('start',start1))
token.dispatcher.add_handler(CommandHandler('website',website))
token.dispatcher.add_handler(CommandHandler('help' , help1))

token.start_polling()
token.idle()
