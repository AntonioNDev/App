import json
import requests


response = requests.get("https://api.weatherapi.com/v1/forecast.json?key=d544248570e94c51a67211516211806&q=Kumanovo&days=2&aqi=yes&alerts=yes").json()

with open("data.json", "w+") as data:
   json.dump(response, data, indent=4)


