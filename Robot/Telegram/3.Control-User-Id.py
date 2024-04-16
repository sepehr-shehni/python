from telegram.ext import Updater , CommandHandler

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context=True)

def start1(update , context):
    context.bot.send_message(text='سلام {} به ربات تک وان 24 خوش امدید . \n برای اطلاعات بیشتر روی دستور /help   کلیک نماییید.'.format(update.message.from_user.first_name),chat_id=update.message.chat_id)
    context.bot.send_message(chat_id= update.message.chat_id , text= 'id : {} \n user : {} \n firstname : {}'.format(update.message.chat_id , update.message.from_user.username ,update.message.from_user.first_name ))
    print(update.message)
def website(update , context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'وبسایت ما :n\ https://techone24.com')
def help1 (update , context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'برای دریافت ادرس وب سایت ما از دستور /website  استفاده کنید \n برای شروع مجدد ربات از /start  استفاده نمایید.\n برای دسترسی به پنل ادمین از دستور /admin  استفاده کنید. ')
def admin (update , context):
    if update.message.chat_id != 870856598:
        context.bot.send_message(chat_id= 87085659 , text= '✅ کاربر با چت آیدی {} وارد ربات شد. ✅'.format(update.message.chat_id))

    else:
        context.bot.send_message(chat_id= update.message.chat_id , text= "شما ادمین هستید و کاربر جدیدی وارد نشده !")


token.dispatcher.add_handler(CommandHandler('start',start1))
token.dispatcher.add_handler(CommandHandler('website',website))
token.dispatcher.add_handler(CommandHandler('help' , help1))
token.dispatcher.add_handler(CommandHandler('admin' , admin))

token.start_polling()
token.idle()
