import os
import time
from random import random
from twython import Twython


CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21

# RUN_EVERY_N_SECONDS = 86400 # e.g. 60*5 = tweets every five minutes
today = date.today()

USERS_TO_IGNORE = []
DO_NOT_FAVORITE_USERS_AGAIN = True

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def favorite_tweet(tweet, handle):
    handle.create_favorite(id=tweet['id'])

def get_urls_of_media_in_tweet(tweet):
    """
    get the urls of media contained in a tweet
    """
    if 'entities' not in tweet or 'media' not in tweet['entities']:
        return []
    return [x['media_url'] for x in tweet['entities']['media']]

def get_mentions(handle, include_entities=False):
    """
    returns iterator of tweets mentioning us
        if you want to get media in tweets, include_entities must be True
    """
    return handle.cursor(handle.get_mentions_timeline,
        include_entities=include_entities)

def get_images_in_mentions(handle):
    """
    check for tweets that mention you, and get the urls of media in those tweets

    e.g., this might be helpful if you make a twitter bot where users can mention you in tweets containing photos, and your bot replies with an altered version of that photo
    """
    for tweet in get_mentions(handle, include_entities=True):
        urls = get_urls_of_media_in_tweet(tweet)
        yield urls

def submit_tweet_with_media(message, mediafile, tweet_to_reply=None, handle=None):
    """
    imfile is the path to an media
    tweet_to_reply is a tweet that you're replying to, if not None
    """
    if not handle:
        handle = twitter_handle()
    media_ids = handle.upload_media(media=open(mediafile))
    if tweet_to_reply is None:
        handle.update_status(status=message,
            media_ids=media_ids['media_id'])
    else:
        # must mention user's name for it to be a reply
        message += ' @' + tweet_to_reply['user']['screen_name']
        handle.update_status(status=message,
            in_reply_to_status_id=tweet_to_reply['id'],
            media_ids=media_ids['media_id'])

def submit_tweet(message, tweet_to_reply=None, handle=None):
    """
    tweet_to_reply is a tweet that you're replying to, if not None
    """
    if not handle:
        handle = twitter_handle()
    if tweet_to_reply is None:
        handle.update_status(status=message)
    else:
        # must mention user's name for it to be a reply
        message += ' @' + tweet_to_reply['user']['screen_name']
        handle.update_status(status=message,
            in_reply_to_status_id=tweet_to_reply['id'])

def get_message(handle):
    """
    Your code goes here!
    """
photo = open('./output/shop.png', 'rb')	    
tweetStr = "Fortnite item shop for "+today.strftime("%m/%d/%y")+"!\n\nIf you want to support me, make sure to use code \"KuletXCore\" on the Fortnite Item Shop!\nReally appreciate it!"

api = twitter_handle()	
response = api.upload_media(media=photo)	
api.update_status(status=tweetStr, media_ids=[response['media_id']])	

print("Tweeted: " + tweetStr)

def main():
    handle = twitter_handle()
    USERS_TO_IGNORE.extend([x['user']['id'] for x in handle.get_favorites()])
    while True:
        message = get_message(handle)
        print(message)
        submit_tweet(message, handle)
        # random_favoriting(['apples', 'oranges'], handle)
        # time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
