
# coding: utf-8

# In[14]:

import sklearn
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import pandas
from sklearn.cross_validation import train_test_split
import numpy


# In[15]:

tweet = pandas.read_csv("C:/c/Rawls/kaggle/twitter/data/Tweets.csv")
tweet.head()


# In[16]:

# percentage of null values in each row
# (total row number - row number in each column)/total row number 
(len(tweet)-tweet.count())/len(tweet)


# In[17]:

del tweet['airline_sentiment_gold']
del tweet['negativereason_gold']
del tweet['tweet_coord']


# In[18]:

mood_count = tweet['airline_sentiment'].value_counts()
mood_count


# In[20]:

Index = [1,2,3]
plt.bar(Index, mood_count)
plt.xticks(Index, ['Negative', 'Neutral', 'Positive'])
plt.ylabel('Mood Count')
plt.xlabel('Moods')
plt.title('Count of Moods')


# In[22]:

tweet['airline'].value_counts()


# In[26]:

def plot_sub_sentiment(Airline):
    df = tweet[tweet['airline'] == Airline]
    count = df['airline_sentiment'].value_counts()
    Index = [1,2,3]
    plt.bar(Index, count)
    plt.xticks(Index, ['Negative', 'Neutral', 'Positive'])
    plt.ylabel('Mood Count')
    plt.xlabel('Moods')
    plt.title('Count of Moods of ' +Airline)
plt.figure(1,figsize=(12,12))
plt.subplot(231)
plot_sub_sentiment('United')
plt.subplot(232)
plot_sub_sentiment('US Airways')
plt.subplot(233)
plot_sub_sentiment('American')
plt.subplot(234)
plot_sub_sentiment('Southwest')
plt.subplot(235)
plot_sub_sentiment('Delta')
plt.subplot(236)
plot_sub_sentiment('Virgin America')


# In[27]:

NR_Count = dict(tweet['negativereason'].value_counts(sort=False))


# In[ ]:

def NR_Count(Airline):
    if Airline == 'All'
        df = tweet
    else:
        df = tweet[tweet['airline']==Airline]
    count = dict(df['negativereason'].value_counts())
    Unique_reason = list(tweet['negativereason'].unique())
    UNique_reason = [x for x in Unique_reason if str(x) != 'nan'] ###
    

