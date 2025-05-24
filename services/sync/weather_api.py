import requests

from config.settings import settings


def now(city: str, latitude: float, longitude: float):
    params = {"units": "metric", "q": city, "lat": latitude, "lon": longitude, "appid": settings.WEATHER_APIKEY}
    response = requests.get(url=settings.WEATHER_API_CALL, params=params).json()

    city_name = response["name"]
    temp = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    
    return {"city_name": city_name, "temp": temp, "feels_like": feels_like}
