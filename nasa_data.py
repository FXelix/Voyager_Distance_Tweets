
import requests
import os


def get_apod():

    os.makedirs("APODs", exist_ok=True)
    try:
        apod_data = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").json()
        image_url = apod_data["url"]
        image_data = requests.get(image_url, stream=True)
    except requests.HTTPError:
        return

    with open(os.path.join("APODs", os.path.basename(image_url)), "wb") as imagefile:
        for chunk in image_data.iter_content(100000):
            imagefile.write(chunk)
        return os.path.abspath((os.path.join("APODs", os.path.basename(image_url))))

