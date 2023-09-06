import json
import requests


req = requests.get("https://api.weatherapi.com/v1/forecast.json?key=d544248570e94c51a67211516211806&q=Kumanovo&days=3&aqi=yes&alerts=yes").json()


with open("newStyle/data.json", "w+") as data:
   json.dump(req, data, indent=4)