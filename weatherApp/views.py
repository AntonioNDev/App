from django.shortcuts import render
from django import forms
import requests
# Create your views here.


class cityNameForm(forms.Form):
   cityName = forms.CharField(label="", min_length=5, widget=forms.TextInput(attrs={'placeholder': 'ex: "London" '}))

def fetchData(cityName):
   try:
      response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key=d544248570e94c51a67211516211806&q={cityName}&days=2&aqi=no&alerts=no")

      if response.status_code != 400:
         return response.json()

      return False

   except Exception as e:
      return False

def index(request):
   if request.method == "POST":
      form = cityNameForm(request.POST)
      
      if form.is_valid():
         data = form.cleaned_data["cityName"]
         
         response = fetchData(data)
         
         if response != False:

            return render(request, "weatherApp/index.html", {
               #Current weather info#
               "form": cityNameForm(),
               "city": response['location']['name'],
               "country": response['location']['country'],
               "condition": response['current']['condition']['text'],
               "conditionICO": response['current']['condition']['icon'],
               "temp_celsius": int(response['current']['temp_c']),
               "humidity": response['current']['humidity'],
               "wind_mph": response['current']['wind_mph'],
               "cloud": response['current']['cloud'],
               "UV": response['current']['uv'],
               "maxtemp_celsius": response['forecast']['forecastday'][1]['day']['maxtemp_c'],
               "mintemp_celsius": response['forecast']['forecastday'][1]['day']['mintemp_c'],
               "chance_of_rain": response['forecast']['forecastday'][1]['day']['daily_chance_of_rain'],
               "is_day": response['current']['is_day'],
               "last_updated": response['location']['localtime'],
               "pressure": response['current']['pressure_mb']

               #Forecast for tomorrow#

            })

         else:
            return render(request, 'weatherApp/layout.html', {
               'form': form,
               'error': 'Something went wrong, try again.'
            })


   return render(request, "weatherApp/layout.html", {
            "form": cityNameForm()
         }) 

