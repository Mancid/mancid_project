import os


HOST = os.environ["HOST_MONGO_DB"]
PASSWORD = os.environ["PASSWORD_MONGO_DB"]
PARKING_SERVER = os.environ["PARKING_SERVER"]
TRAM_SERVER = os.environ["TRAM_SERVER"]
VELO_SERVER = os.environ["VELO_SERVER"]
AUTH_SERVER = os.environ["AUTH_SERVER"]

URL_VELOCITY = "https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml"

URL_WEATHER = "http://api.openweathermap.org/data/2.5/weather?q=Montpellier,fr&lang=fr&APPID=beb97c1ce62559bba4e81e28de8be095&units=metric"

URL_FORECAST = "http://api.openweathermap.org/data/2.5/forecast?q=Montpellier,fr&lang=fr&APPID=beb97c1ce62559bba4e81e28de8be095&units=metric"
