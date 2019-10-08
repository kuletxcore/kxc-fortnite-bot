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


tweetStr = "This bot will post this RWBY playlist every day until @DonaldMustard watches it, or if an official @FortniteGame x @OfficialRWBY collab/crossover happens.\nhttps://www.youtube.com/playlist?list=PL2Oan_kP2lqq2Kc1_tzbYniNWwklzStG1\n\n[Automatically Posted]"

api = twitter_handle()
api.update_status(status=tweetStr)	

print("Tweeted: " + tweetStr)
