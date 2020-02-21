#!/usr/bin/env python
# coding: utf-8

# In[2]:


CONSUMER_KEY = 'a19MLVL0NMt7ByLp74Ey0hFN7'
CONSUMER_KEY_SECRET = 'q2KiIFKpwoLqXIIOjNAZ4zEm8h9Vmvwp8X3drcr0WeiLepdJYt'
ACCESS_TOKEN = '1167467648181035008-8PqoqisYZTNwAHxvmd6QqYmH2ztS6a'
ACCESS_TOKEN_SECRET = 'FnXJhL4a50kSTb5Bzr1Ix6cIfnXG6XxvrAPtPU7gmiyal'

import tweepy
import csv
from textblob import TextBlob

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

csvFile = open('#freetommy.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#freetommy",  count=100000,                            lang="en",                            since_id=2019 - 10 - 17).items():
        print(tweet.created_at, tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment_assessments)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), analysis.polarity, analysis.subjectivity])


# In[ ]:




