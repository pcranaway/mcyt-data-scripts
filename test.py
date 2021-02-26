import collector

tweet = '''RT by @joe #clingytwt matching pfps?? (credit me if you use em 😩‼️)
#tubbofanart #tubboart #tommyinnitfanart #TOMMYINNIT #mcyt #mcyttwt'''

# tweet = collector.fix_title(tweet)
tweet = collector.remove_hashtags(tweet)

print(tweet)
