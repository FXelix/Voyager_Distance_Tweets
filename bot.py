
import tweepy
from secrets import *
from voyager_distance import get_distance

# standard for accessing Twitter API
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(get_distance())
