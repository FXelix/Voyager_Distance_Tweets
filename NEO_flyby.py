
import datetime
import requests
from math import log10


class NEO:
    """
    To access the data, corresponding numbers:
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
    h = 10
    """

    json_data = requests.get("https://ssd-api.jpl.nasa.gov/cad.api?body=Earth&dist-max=20LD").json()

    neo_data = []

    @staticmethod
    def diameter_calc(log_value, mag):
        #formula for diamter calculation
        return 10**(0.5*(6.259 - log10(log_value) - 0.4*mag))

    def flyby_data(self):

        # unix = time.time()
        # datestamp = datetime.datetime.fromtimestamp(unix).strftime("%Y-%b-%d")

        # better way to do it:
        now = datetime.datetime.now()
        datestamp = "{:%Y-%b-%d}".format(now)

        for data in self.json_data["data"]:

            neo_date = data[3][:11]
            neo_time = data[3][12:]
            neo_des = data[0]
            magnitude = float(data[10])

            diameter_min = self.diameter_calc(0.25, magnitude)
            diameter_max = self.diameter_calc(0.05, magnitude)

            if neo_date == datestamp:
                self.neo_data.append((neo_des, neo_time, round(diameter_min,4), round(diameter_max,4)))
                
        return self.neo_data
