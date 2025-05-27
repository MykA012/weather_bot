from datetime import datetime, timedelta

import requests

from config.settings import settings
from database.weather_ids import ids


def validate_city(city: str) -> bool:
    params = {"q": city, "appid": settings.WEATHER_APIKEY}
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather", params=params
    )

    return response.status_code == 200


def today(
    city: str = None, latitude: float = None, longitude: float = None
) -> dict[str:str]:
    params = {
        "q": city,
        "lat": latitude,
        "lon": longitude,
        "units": "metric",
        "lang": "ru",
        "appid": settings.WEATHER_APIKEY,
    }
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather", params=params
    ).json()

    if response["cod"] != 200:
        raise requests.HTTPError

    icon = ids[response["weather"][0]["id"]]["emoji"]
    name = response["name"]
    description = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]

    return {
        "icon": icon,
        "name": name,
        "description": description,
        "temp": temp,
        "feels_like": feels_like,
    }


def tomorrow(
    city: str = None, latitude: float = None, longitude: float = None
) -> dict[str:str]:
    params = {
        "q": city,
        "lat": latitude,
        "lon": longitude,
        "units": "metric",
        "lang": "ru",
        "appid": settings.WEATHER_APIKEY,
    }
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/forecast", params=params
    ).json()

    if response["cod"] != "200":
        raise requests.HTTPError

    tomorrow_date = (
        f"{(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")} 12:00:00"
    )

    forecast = [item for item in response["list"] if item["dt_txt"] == tomorrow_date][0]

    icon = ids[forecast["weather"][0]["id"]]["emoji"]
    name = response["city"]["name"]
    description = forecast["weather"][0]["description"]
    temp = forecast["main"]["temp"]
    feels_like = forecast["main"]["feels_like"]

    return {
        "icon": icon,
        "name": name,
        "description": description,
        "temp": temp,
        "feels_like": feels_like,
    }
