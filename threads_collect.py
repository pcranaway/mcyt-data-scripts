from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
import requests
import datetime
import random

NITTER_INSTANCES = [
    'https://nitter.42l.fr',
    'https://nitter.nixnet.services',
    'https://nitter.13ad.de',
    'https://nitter.pussthecat.org',
    'https://nitter.mastodont.cat',
    'https://nitter.tedomum.net',
    'https://nitter.fdn.fr',
    'https://nitter.1d4.us',
    'https://nitter.kavin.rocks',
    'https://tweet.lambda.dance',
    'https://nitter.cc',
    'https://nitter.weaponizedhumiliation.com',
    'https://nitter.vxempire.xyz',
    'https://nitter.unixfox.eu',
    'https://nitter.domain.glass',
    'https://nitter.himiko.cloud',
    'https://nitter.eu',
    'https://nitter.ethibox.fr',
    'https://nitter.namazso.eu',
    'https://nitter.mailstation.de',
    'https://nitter.actionsack.com',
    'https://nitter.cattube.org',
]

ENDPOINT = ''
PATH = '/search?f=tweets&q=%23{}&since={}&until={}&near='
HASHTAGS = ['mcyt', 'mcyttwt']
TODAY = datetime.date.today()
ONE_DAY = datetime.timedelta(days=1)

since = TODAY - ONE_DAY
until = TODAY
i = 0

def fmtdate(date):
    return '{}-{}-{}'.format(date.year, date.month, date.day)

def rotate_nitter():
    global ENDPOINT
    ENDPOINT = random.choice(NITTER_INSTANCES)

rotate_nitter()

while True:
    if i > 0:
        since -= ONE_DAY
        until -= ONE_DAY

    if i % 2 == 0:
        rotate_nitter()

    i += 1

    for hashtag in HASHTAGS:
        try:
            url = ENDPOINT + PATH.format(hashtag, fmtdate(since), fmtdate(until))

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            tweets = soup.find_all('div', {'class': 'timeline-item'})

            for tweet in tweets:
                content = tweet.find('div', {'class': 'tweet-content'})
                elements = content.contents
                links = []
                text = []

                for element in elements:
                   
                    if type(element) == Tag:
                        links.append(element.contents[0])

                    if type(element) == NavigableString:
                        string = str(element)

                        if not (string == ' ' or string == ''):

                            string = string.strip()
                            string = string.replace('\n', '')

                            text.append(string)

                text = ' '.join(text)
                # print(text)

                thread = tweet.find('a', {'class': 'tweet-link'})
                # print(thread['href'])

                for link in links:
                    if link.startswith('#'):
                        print(link)

        except Exception as ex:
            pass
