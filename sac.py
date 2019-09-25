#!/usr/bin/env python
import sys
import os
import time
from twython import Twython, TwythonError

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21

# RUN_EVERY_N_SECONDS = 86400 # e.g. 60*5 = tweets every five minutes

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('./output/SAC_Reminder.png', 'rb')
tweetStr = "Weekly Reminder that FN codes expire every Fortnight! (aka 14 days!)\nUse code \"KuletXCore\" in the shop if you want to support me!\n\n[Automatically Posted]"

api = twitter_handle()
response = api.upload_media(media=photo)	
api.update_status(status=tweetStr, media_ids=[response['media_id']])	

print("Tweeted: " + tweetStr)
