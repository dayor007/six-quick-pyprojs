import requests
from pprint import pprint

API_Key = 'b7bed88121e0b6f8e40c578b73768f40'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data  = requests.get(base_url).json()

pprint(weather_data)