
import time
import datetime
import requests
import json


class NEO:

    des = 0
    orbit_id = 1
    jd = 2
    cd = 3
    dist = 4
    dist_min = 5
    dist_max = 6
    v_rel = 7
    v_inf = 8
    t_signma_F = 9
    body = 10
    h = 11

    json_data_url = requests.get("https://ssd-api.jpl.nasa.gov/cad.api?body=Earth&dist-max=20LD")
    json_data = json.loads(json_data_url.text)

    neo_data = []

    def estimated_diameter(self):
        # todo

    def flyby_data(self):

    unix = time.time()
    datestamp = datetime.datetime.fromtimestamp(unix).strftime("%Y-%b-%d")

    for i in range(len(json_data["data"])):
        neo_date = json_data["data"][i][cd][:11]
        neo_time = json_data["data"][i][cd][11:]
        neo_des = json_data["data"][i][des]

        if neo_date == datestamp:
            neo_data.append((neo_des, neo_time,))







        
        # sorte lieber per magnitude und nimm nur das größte objekt, sonst ist der tweet zu lang



# TODO: Iterate over data and return tuple


