import telebot 
from telebot import *
import webbrowser
from translate import *


bot = telebot.TeleBot("6453371055:AAGYzwcUf9IjLH7K-4a48pqrJWKwBtiSnCk")
print('Runnig Telegram bot...')



@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} \n I am UbiLingo translater of your any text.')
    
    
    markup = types.InlineKeyboardMarkup()
    english  = types.InlineKeyboardButton('ENGLISH' , callback_data='english')
    german  = types.InlineKeyboardButton('GERMAN' , callback_data='german')
    markup.row(english, german)
    french = types.InlineKeyboardButton('FRENCH', callback_data='french')
    japanese = types.InlineKeyboardButton('JAPANESE', callback_data='japanese')
    markup.row(french,japanese)
    turkish = types.InlineKeyboardButton('TURKISH', callback_data='turkish')
    chinese = types.InlineKeyboardButton('CHINESE' , callback_data='chinese')
    markup.row(turkish,chinese)
    russian = types.InlineKeyboardButton('RUSSIAN', callback_data='russian')
    markup.row(russian)
    
    bot.reply_to(message,'Choose the language you want to translate from:',reply_markup=markup )



@bot.callback_query_handler(func=lambda callback :True)
def callback_message(callback):
    global from_lang1
    match callback.data:
        case 'english':
            from_lang1 = 'en'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'german':
            from_lang1 = 'de'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'french':
            from_lang1 = 'fr'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'japanese':
            from_lang1 = 'japanese'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'turkish':
            from_lang1 = 'tr'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'chinese':
            from_lang1 = 'chinese'
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
        case 'russian':
            from_lang1 = 'ru'   
            bot.delete_message(callback.message.chat.id , callback.message.message_id)
            bot.delete_message(callback.message.chat.id , callback.message.message_id-1)

    markup = types.InlineKeyboardMarkup()
    english2  = types.InlineKeyboardButton('ENGLISH' , callback_data='english2')
    german2  = types.InlineKeyboardButton('GERMAN' , callback_data='german2')
    markup.row(english2, german2)
    french2 = types.InlineKeyboardButton('FRENCH', callback_data='french2')
    japanese2 = types.InlineKeyboardButton('JAPANESE', callback_data='japanese2')
    markup.row(french2,japanese2)
    turkish2 = types.InlineKeyboardButton('TURKISH', callback_data='turkish2')
    chinese2 = types.InlineKeyboardButton('CHINESE' , callback_data='chinese2')
    markup.row(turkish2,chinese2)
    russian2 = types.InlineKeyboardButton('RUSSIAN', callback_data='russian2')
    markup.row(russian2)
    
    bot.send_message(callback.message.chat.id,'Choose the language you want to translate to:',reply_markup=markup)

    global to_lang1
    match callback.data:
        case 'english2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'en'
        case 'german2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'de'
        case 'french2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'fr'
        case 'japanese2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'japanese'
        case 'turkish2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'tr'
        case 'chinese2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'chinese'
        case 'russian2':
            bot.delete_message(callback.message.chat.id , callback.message.message_id) 
            bot.send_message(callback.message.chat.id , 'Ok, now you can type any text for translating')   
            to_lang1 = 'ru'     
    bot.delete_message(callback.message.chat.id , callback.message.message_id) 
    

@bot.message_handler()
def translating(message):
    translator = Translator(from_lang = from_lang1,to_lang= to_lang1)
    global message_1 
    bot.send_message(message.chat.id, translator.translate(message.text))



bot.polling(non_stop=True)

    