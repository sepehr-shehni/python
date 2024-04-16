from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
from telegram import ParseMode , MessageEntity

token = Updater('6743517165:AAEDmyIQ4bJ2kIEUfrUHerHEziDcnG3ec8I' , use_context=True)

def start(update , context):
    context.bot.send_message(chat_id= update.message.chat_id , text= 'سلام{} به ربات ضد لینک تک وان 24 خوش امدید'.format(update.message.from_user.first_name))
def antilink(update, context):
    list_1 = [MessageEntity.URL]
    if update.message.parse_entities(types=list_1):
        context.bot.delete_message(chat_id = update.message.chat_id , message_id= update.message.message_id)

def antilink_files(update , context):
    if update.message.caption_entities[0]['type'] == 'url':
        context.bot.delete_message(chat_id= update.message.chat_id , message_id= update.message.message_id)


token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(MessageHandler(Filters.all , antilink))
token.dispatcher.add_handler(MessageHandler(Filters.all , antilink_files))

token.start_polling()
token.idle()
