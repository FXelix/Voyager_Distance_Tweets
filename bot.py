
import tweepy
from secrets import *
from voyager_distance import get_distance
from NEO_flyby import NEO

# standard for accessing Twitter API
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(get_distance())

for data in NEO().flyby_data():
    try:
        new_neo = "Today's NEO: Object: {} at {}. Estimated diameter: {} - {} km.".format(*data)
        api.update_status(new_neo)
    except IndexError:
        pass
