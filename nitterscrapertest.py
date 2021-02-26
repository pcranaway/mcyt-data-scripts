from pprint import pprint
from nitter_scraper import NitterScraper
import time

last_tweet_id = None

with NitterScraper(host="0.0.0.0", port=8008) as nitter:

    while True:
        for tweet in nitter.get_tweets("pcranaway", pages=1, break_on_tweet_id=last_tweet_id):

            if tweet.tweet_id != last_tweet_id:
                print(tweet.json(indent=4))

            last_tweet_id = tweet.tweet_id

            break

            time.sleep(0.1)
