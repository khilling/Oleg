import requests
from bs4 import BeautifulSoup
import telebot
import random


def panorama_article():
    home_url = 'https://panorama.pub'
    page = requests.get(home_url)
    unpretty_text = page.text
    soup = BeautifulSoup(unpretty_text, 'html.parser')
    new_url = soup('a', rel = 'bookmark')[random.randint(0, 15)]['href']
    new_page_text = requests.get(new_url).text
    new_soup = BeautifulSoup(new_page_text, 'html.parser')
    article = list(map(str, new_soup.findAll('p')))[2:-1]
    article = '\n'.join([i[3:-4] for i in article])
    return article    
    

opb_token = '1034547759:AAFr2tHhzuccOW3IhS-UQ29kvskqgomkWGs'    #Oleg_Panorama_Bot
bot = telebot.TeleBot(opb_token)

@bot.message_handler(commands = ['start', 'help'])
def get_text_messages(message):
    bot.reply_to(message, 'text me PANORAMA if u want to see a meme')

@bot.message_handler(content_types = ['text'])
def send_article(message):
    if message.text == 'PANORAMA':
        bot.reply_to(message, panorama_article())
    else:
        bot.reply_to(message, 'register is important, text me PANORAMA')
	

bot.polling(none_stop = True, interval = 0)