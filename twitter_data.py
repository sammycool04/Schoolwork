
import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
access_token = "952850784-MdMpt7kmUXTpyVIA0tYVDsOLoxorzZUBZVqIcq5l"
access_token_secret="TBjG3omG8q0mK79jJTiBK4zGJ6qV2ZL7J1aZb0bLMJalD"
consumer_key="gJcYfKUC9Jw5riJPkB1J5Rcii"
consumer_secret="fcIAbs8V8DZTyC8BaXzfducrQUybiXmowWc24ArVkjEDxg08jI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 10000:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

def word_in_text(word,tweet):
    word = word.lower()
    text=tweet.lower()
    match = re.search(word,tweet)

    if match:
        return True
    return False

l=MyStreamListener()
stream = tweepy.Stream(auth,l)
stream.filter(track=['school','homework','final','fun'])

tweets_data_path='tweets.txt'
tweets_data =[]
tweets_file = open(tweets_data_path,'r')
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0].keys())
df = pd.DataFrame(tweets_data,columns=['text','lang'])
print(df.head())

[school,homework,final,fun]=[0,0,0,0]
for index, row in df.iterrows():
    school += word_in_text('school', row['text'])
    homework += word_in_text('homework', row['text'])
    final += word_in_text('final', row['text'])
    fun += word_in_text('fun', row['text'])
sns.set(color_codes=True)
cd = ['school','homework','final','fun']
ax=sns.barplot(cd,[school,homework,final,fun])
ax.set(ylabel = 'count')
plt.show()
