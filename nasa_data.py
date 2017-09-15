
import requests
import os


def get_apod():

    os.makedirs("APODs", exist_ok=True)
    try:
        # check if website is accessible
        apod_data = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        apod_data.raise_for_status()
        apod_data = apod_data.json()

        # check if image is accessible
        image_url = apod_data["url"]
        image_data = requests.get(image_url, stream=True)
        image_data.raise_for_status()
    except requests.HTTPError:
        return

    # if APOD is no image; bot.py uses get_url for video url's instead
    if not image_url.endswith((".gif",".jpeg",".jpg")):
        return

    with open(os.path.join("APODs", os.path.basename(image_url)), "wb") as imagefile:
        for chunk in image_data.iter_content(100000):
            imagefile.write(chunk)

    # Twitter limitation: .gif must be smaller than 3MB
    if image_url.endswith(".gif") and os.path.getsize(os.path.join("APODs", os.path.basename(image_url))) >= 3145728:
        return

    else:
        return os.path.abspath((os.path.join("APODs", os.path.basename(image_url))))


def get_url():

    os.makedirs("APODs", exist_ok=True)
    try:
        # check if website is accessible
        apod_data = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        apod_data.raise_for_status()
        apod_data = apod_data.json()

        # check if image is accessible
        image_url = apod_data["url"]
        image_data = requests.get(image_url, stream=True)
        image_data.raise_for_status()
    except requests.HTTPError:
        return

    return image_url

