import requests
import json



res = requests.get("https://api.weatherapi.com/v1/forecast.json?key=d544248570e94c51a67211516211806&q=Hawai&days=2&aqi=no&alerts=yes").json()



with open('data.json', 'w+') as data:
   json.dump(res, data, indent=4)

""" for x in range(len(res['alerts']['alert'])):
   print(res['alerts']['alert'][x]['headline']) """