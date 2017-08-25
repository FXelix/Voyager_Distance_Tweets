
import requests
import bs4


def get_distance():
    res_1 = requests.get("https://theskylive.com/voyager1-tracker")
    res_2 = requests.get("https://theskylive.com/voyager2-tracker")

    try:
        res_1.raise_for_status()
        res_2.raise_for_status()
    except Exception as exc:
        print(f"Error {exc}")

    soup1 = bs4.BeautifulSoup(res_1.text, "html.parser")
    soup2 = bs4.BeautifulSoup(res_2.text, "html.parser")

    distance_element_1 = soup1.select("#disearth")
    distance_element_2 = soup2.select("#disearth")

    print("Voyager I is now {} km from Earth.".format(distance_element_1[0].getText()))
    print("Voyager II is now {} km from Earth.".format(distance_element_2[0].getText()))

get_distance()

