import stweet as st
import arrow

task = st.SearchTweetsTask(
    '#mcyt', '#mcyttwt',

    since=arrow.get('2020-01-1'),
    until=arrow.get('2021-12-1')
)

tweets_collector = st.CollectorTweetOutput()
result = st.TweetSearchRunner(task, [tweets_collector, st.JsonLineFileTweetOutput('mcyt_tweets.json')]).run()
print(f'scrapping task result: {result}')
