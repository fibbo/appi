""" Users/philippg/projects/appi/src/weather_report.py
"""

import json
import os
from typing import final

import requests
from typing_extensions import override

api_key = os.getenv("NINJA_API_KEY")


@final
class City:
    def __init__(self, info_dictionary: dict[str, str]):
        self.name = info_dictionary["name"]
        self.lat = info_dictionary["latitude"]
        self.lon = info_dictionary["longitude"]
        self.country = info_dictionary["country"]
        self.state = info_dictionary.get("state", "")

    @override
    def __str__(self):
        return (
            f"City({self.name}, {self.country}, {self.state}, {self.lat}, {self.lon})"
        )

    # So when we a list of cities we can print them nicely
    __repr__ = __str__


def get_cities_geo_code(city_name: str, country_name: str) -> list[City]:
    api_url = f"https://api.api-ninjas.com/v1/geocoding?city={city_name}"
    country_parameter = f"&country={country_name}" if len(country_name) > 0 else ""
    api_url += country_parameter

    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    cities = []
    if response.status_code == requests.codes.ok:
        for result in response.json():
            cities.append(City(result))
    return cities


def get_weather(cities: list[City], weather: dict) -> None:
    for city in cities:
        api_url = f"https://api.api-ninjas.com/v1/weather?lat={city.lat}&lon={city.lon}"
        response = requests.get(api_url, headers={"X-Api-Key": api_key})
        if response.status_code == requests.codes.ok:
            if f"{city.name}|{city.state}|{city.country}" in weather:
                weather[f"{city.name}|{city.state}|{city.country}"].append(
                    response.json()
                )
            else:
                weather[f"{city.name}|{city.state}|{city.country}"] = [response.json()]
            print(
                f"Weather for {city.name} in {city.state}, {city.country}: {response.text}"
            )
        else:
            print("Error:", response.status_code, response.text)

    with open("weather.json", "w") as f:
        json.dump(weather, f)


with open("weather.json") as f:
    weather = json.load(f)


city = input("City: ")
country = input("Country (optional): ")

cities = get_cities_geo_code(city, country)
get_weather(cities, weather)
