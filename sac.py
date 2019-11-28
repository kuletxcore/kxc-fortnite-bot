#!/usr/bin/env python

#Please do not change anything to this section!
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


def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('./output/SAC_Reminder.png', 'rb')

#Change the text into anything you like!
tweetStr = "Weekly Reminder that Fortnite codes expire every Fortnight! (aka 14 days!)\nPLEASE USE A SUPPORT-A-CREATOR CODE! It doesn’t have to be me, just a creator you really like. \nBut if you would like to support me, please use code \"KuletXCore\" in the Item shop! Thank you!\n\n[Automatically Posted]"

api = twitter_handle()
response = api.upload_media(media=photo)	
api.update_status(status=tweetStr, media_ids=[response['media_id']])	

print("Tweeted: " + tweetStr)
