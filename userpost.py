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

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

tweetStr = "Fortnite Battle Royale News Feed update for "+today.strftime("%m/%d/%y")+"!\n\n[Automatically Posted]"

api = twitter_handle()
api.update_status(status=tweetStr)

print("Tweeted: " + tweetStr)
