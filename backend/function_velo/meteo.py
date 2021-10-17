import requests
from backend.variable import URL_WEATHER, URL_FORECAST


def conf():
    r_weather = requests.get(URL_WEATHER)
    data = r_weather.json()
    temp = round(data['main']['temp'])
    cond = data['weather'][0]['description']
    return temp, cond


def data():
    result = {}
    r_forecast = requests.get(URL_FORECAST)
    data = r_forecast.json()
    for i in range(0, 25):
        t = data['list'][i]['main']['temp']
        temps = data['list'][i]['weather'][0]['description']
        time = data['list'][i]['dt_txt']
        result[i] = f'{time}, {t}, {temps}'
    return result


def get_meteo_at_nine():
    result = {}
    for v in data().values():
        if v[11:16] == "09:00":
            result["date"] = v[0:10]
            result["heure"] = v[11:16]
            result["temps"] = v[21:25]
            result["conditions"] = v[27:]
            return result
