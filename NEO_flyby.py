
import time
import datetime
import requests
import json
from math import log10


class NEO:
    """
    For accesing the data, corresponding numbers:
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
    """
    json_data_url = requests.get("https://ssd-api.jpl.nasa.gov/cad.api?body=Earth&dist-max=20LD")
    json_data = json.loads(json_data_url.text)

    neo_data = []

    def flyby_data(self):

        unix = time.time()
        datestamp = datetime.datetime.fromtimestamp(unix).strftime("%Y-%b-%d")

        for i in range(len(self.json_data["data"])):
            neo_date = self.json_data["data"][i][3][:11]
            neo_time = self.json_data["data"][i][3][11:]
            neo_des = self.json_data["data"][i][0]
            diameter_min = 10 ** 0.5*(6.259 - log10(0.05) - 0.4 * self.json_data["data"][i][11])
            diameter_max = 10 ** 0.5*(6.259 - log10(0.25) - 0.4 * self.json_data["data"][i][11])

            if neo_date == datestamp:
                self.neo_data.append((neo_des, neo_time, diameter_min, diameter_max))
                
        return self.neo_data
