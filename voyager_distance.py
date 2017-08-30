
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

    distance_voyager_1 = int(distance_element_1[0].getText())
    distance_voyager_2 = int(distance_element_2[0].getText())

    return (distance_voyager_1, distance_voyager_2)
