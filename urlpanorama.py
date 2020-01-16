import requests
from bs4 import BeautifulSoup
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


print(panorama_article())