import pandas as pd
import requests as requests
import base64
import tweepy
from tweepy import OAuthHandler
from pandas.io.json import json_normalize
import unicodedata

#Define your keys from the developer portal from Twitter
client_key = 'xxxxxxxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxx'
access_token_secret ='xxxxxxxxxxxxxxxxxx'

auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

bareer_key = 'xxxxxxxxxxxxxxxxxx'
headers = {"Authorization": "Bearer {}".format(bareer_key)}

def getFriends(usuario, header):

  api_url = 'https://api.twitter.com/1.1/friends/list.json'
  return requests.get(api_url, headers = header,
                        params={"screen_name" : usuario,
                        "skip_status" : "t",
                        "count": "42"}).json()
  
  
def getTweetsByHashtag(hashtag, header):
  api_url = 'https://api.twitter.com/1.1/search/tweets.json'
  return requests.get(api_url, headers = header,
                            params={"q": hashtag}).json()


data = getFriends('user', headers)
tweets = getTweetsByHashtag("#topic", headers)


tweets_df = pd.DataFrame(tweets["statuses"])
print(tweets_df["text"].head())


data_types = {
  "id_str" : int,
  "name": str,
  "screen_name": str,
  "location": str,
  "description": str,
  "url": str,
  "followers_count":str,
  "friends_count":str

}

flat_data = pd.DataFrame(data["users"], dtype = str)

print(flat_data.dtypes) 

print(flat_data.iloc[:, 0:11].head())


del flat_data['entities']

print(flat_data.dtypes)
flat_data_2 = flat_data[['id','id_str','screen_name', 'followers_count', 'friends_count', 'blocking', 'blocked_by']]

print(flat_data_2)
