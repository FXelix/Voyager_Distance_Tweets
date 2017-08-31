
import requests


def get_APOD():

    picture_data = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").json()


# TODO: get daily image

# TODO: twitter daily image