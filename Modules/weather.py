import requests
import json
import math

def getWeather(city):
    city = city
    api_key = "0f4392845c840fdff2ff0fe72dbd116d"

    final_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)

    result =  requests.get(final_URL)
    data = result.json()
    main = data['weather'][0]['main']
    temp = data['main']['temp']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    city = city.title()

    if main == "Rain":
        status = "Today in {} is raining outside, take your umbrella sir!".format(city)
        return status, temp, min_temp, max_temp

    elif main == "Clouds":
        status = "Today in {} is mostly cloudy sir.".format(city)
        return status, temp, min_temp, max_temp

    elif main == "Clear":
        status = "Today in {} is clear outside, the perfect day to launch a rocket sir.".format(city)
        return status, temp, min_temp, max_temp


