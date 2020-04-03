import sys
import pyowm
import requests

key     = sys.argv[1]
city    = sys.argv[2]

api_call        = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key
api_response    = requests.get(api_call)
response_json   = api_response.json()
response_city   = response_json['name']
response_desc   = response_json['weather'][0]['description']
response_temp   = response_json['main']['temp']
response_hmdt   = response_json['main']['humidity']

print(f'source=openweathermap, city="{response_city}", description="{response_desc}", temp={response_temp}, humidity={response_hmdt}')