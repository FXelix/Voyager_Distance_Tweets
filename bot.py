
import tweepy
from secrets import *
from voyager_distance import get_distance
from NEO_flyby import NEO
from nasa_data import get_apod

# standard for accessing Twitter API
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    voyager_message = "Voyager I is now {:,} km from Earth. \nVoyager II is now {:,} km from Earth. \n#bot #space #voyager".format(*get_distance())
    api.update_status(voyager_message)
except IndexError:
    pass

for data in NEO().flyby_data():
    try:
        new_neo = "Today's NEO: Object: {} at {}. Estimated diameter: {} - {} km. \n#bot #NEO #asteroids".format(*data)
        api.update_status(new_neo)
    except IndexError:
        api.update_status("No near-Earth objects for today! We're save! ...at least for now... \n#bot #doomsday #NEO #asteroids")

try:
    api.update_with_media(get_apod(), status="The Astronomical Picture of the Day by NASA. #bot #NASA #space")
except tweepy.TweepError:
    pass
