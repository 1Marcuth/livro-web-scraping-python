from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import random
import re

random.seed(datetime.now().timestamp())

def get_links(article_url: str):
    html = urlopen(f'http://en.wikipedia.org{article_url}')
    bs = BeautifulSoup(html, 'html.parser')

    links = (bs
        .find('div', id='bodyContent')
        .find_all(
            'a',
            href=re.compile('^(/wiki/)((?!:).)*$')
        ))

    return links

links = get_links('/wiki/Kevin_Bacon')

while len(links) > 0:
    new_article = links[random.randint(
        0,
        len(links) - 1
    )].attrs['href']

    print(new_article)

    links = get_links(new_article)