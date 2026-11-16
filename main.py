import telebot, random, os
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)
print('hey')

#start command
@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.chat.id
    bot.send_message(user,'Hello \n you cracket!!! ')

with open('countries.txt', encoding='utf-8') as f:
    lines = f.readlines()

#main code
@bot.message_handler(content_types=['text'])
def send_text(message):
    user = message.chat.id
    
    if message.text == "help":
        bot.send_message(user,'⛄⛄⛄⛄⛄ cracker ⛄⛄⛄⛄⛄')

    elif message.text == '🤍':
        bot.send_message(user, '⛄⛄⛄⛄')

    elif message.text == 'bye':
        bot.send_message(user, 'well')
        bot.send_message(user, 'see you')

    elif message.text == 'random':
        bot.send_message(user, f'The random number for you is {random.randint(1,10)}')

    elif message.text == 'country':
        bot.send_message(user, f'The random country for you is {random.choice(lines).strip()}')
    
    else:
        bot.send_message(message.chat.id, 'hahaha ¯\_(ツ)_/¯ ')

bot.infinity_polling()
