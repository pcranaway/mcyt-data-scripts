import feedparser
from pprint import pprint

# The hashtags i use mcyt & relevant hashtags because it's a very intriguing community
hashtags = ['mcyt']
# hashtags = ['mcyt', 'mcyttwt', 'tommy', 'tommyinnit']

# The nitter instance
# Find one here - https://github.com/zedeus/nitter/wiki/Instances
# Consider donating to the maintainer of Nitter - https://liberapay.com/zedeus
# 
# TODO: Add support for multiple nitter instances so we don't overload one
ENDPOINT = 'https://nitter.cc'

PATH = '/search/rss?f=tweets&q=%23{}'

def remove_hashtags(text: str):
    """
    removes all hashtags and @mentions from a string
    """

    tokens = text.split(' ')

    for token in tokens:

        token = token.rstrip()
        # token = ' '.join(token.splitlines())

        # if token starts with @ or #, remove it
        if token.startswith('#') or token.startswith('@'):
            text = text.replace(token, '')

        # if token is a link of some sort, remove it
        # (this checks if :// is in the token but i wouldn't be surprised if they started using 
        # that in their tweets kinda like those people that have their usernames as https_(name)
        # if they do, open a pull request and just make it check if it's a http(s) link, please!)
        if '://' in token:
            text = text.replace(token, '')

    return text

def fix_title(title: str):
    """
    Fixes the title (content) of a tweet by removing parts of it that are not part of the actual tweet
    """

    # put all lines into one long string
    title = ' '.join(title.split())

    # remove "RT by" (mentions are removed along with hashtags later)
    title = title.replace('RT by ', '')

    # remove mentions and hashtags
    title = remove_hashtags(title)

    return title

# check if the program ius actually being ran and not included as a module
if __name__ == '__main__':

    # loop through all hashtags and fetch the feed
    for hashtag in hashtags:

        url = ENDPOINT + PATH.format(hashtag)

        feed = feedparser.parse(url)

        # loop through all entries (which in this case, are tweets)
        for tweet in feed.get('entries'):
            pprint(tweet)
            # print()
            
            title = fix_title(str(tweet['title']))
            # print(title)

