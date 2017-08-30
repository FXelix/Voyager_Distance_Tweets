
import time
import datetime
import requests
import json

def get_NEO_flyby():

    neo_data = []


    unix = time.time()
    datestamp = datetime.datetime.fromtimestamp(unix).strftime("%Y-%b-%d")

    json_data_url = requests.get("https://ssd-api.jpl.nasa.gov/cad.api?body=Earth&dist-max=20LD")
    json_data = json.loads(json_data_url.text)
    for i in range(len(json_data["data"])):
        neo_date = json_data["data"][i][3][:11]
        neo_time = json_data["data"][i][3][11:]

        if neo_date == datestamp:
            neo_data.append((json_data["data"][i][0],))




        
        # sorte lieber per magnitude und nimm nur das größte objekt, sonst ist der tweet zu lang



get_NEO_flyby()


# TODO: Add api indicator of numbers
# TODO: Iterate over data and return tuple


