
import tweepy
from secrets import *
from voyager_distance import get_distance
from NEO_flyby import flyby_data
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

if not flyby_data():
    api.update_status("No near-Earth objects for today! We're save! ...at least for now... \n#bot #doomsday #NEO #asteroids")
else:
    try:
        for data in flyby_data():
            new_neo = "Today's NEO: Object: {} at {}. Estimated diameter: {} - {} km. \n#bot #NEO #asteroids".format(*data)
            api.update_status(new_neo)
    except (IndexError or tweepy.TweepError):
        pass

try:
    if not get_apod().endswith((".png",".gif",".jpeg",".jpg")):
        # message with url if APOD is a not an image
        message_video = "The Astronomical Picture of the Day by NASA. \n{} #bot #NASA #space".format(get_apod())
        api.update_status(message_video)
    else:
        # message with image
        api.update_with_media(get_apod(), status="The Astronomical Picture of the Day by NASA. #bot #NASA #space")
except tweepy.TweepError:
    pass
