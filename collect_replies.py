import stweet as st
import arrow
import csv

tweets = []

with open('./sample_tweets.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        id = int(float(row[1]))
        content = row[3]

        tweets.append({
            'id': id,
            'content': content,
            'replies': []
        })

ids = [str(tweet['id']) for tweet in tweets]

print(ids)

try:
    task = st.TweetsByIdsTask(ids)
    outputs = []
    result = st.TweetsByIdsRunner(task, outputs).run()

    print(outputs)
    print(result)

except Exception:
    print('aw :(')
