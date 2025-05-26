import requests

from config.settings import settings


def now(city: str = None, latitude: float = None, longitude: float = None):
    params = {
        "units": "metric",
        "q": city,
        "lat": latitude,
        "lon": longitude,
        "exclude": "current",
        "appid": settings.WEATHER_APIKEY,
        "lang": "ru",
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params).json()

    if response["cod"] != 200:
        raise requests.HTTPError

    name = response["name"]
    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    description = response["weather"][0]["description"]

    return {
        "name": name,
        "temp": temp,
        "feels_like": feels_like,
        "description": description,
    }