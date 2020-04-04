import os
import sys
import pyowm
import requests
import re

class EmptyValue(Exception):
    pass
class InvalidFormat(Exception):
    pass
class ApiError(Exception):
    pass

try:
    key = os.environ['OPENWEATHER_API_KEY']
    key_valid = re.match('\w{32}', key)
    if len(key) == 0:
        raise EmptyValue('Environment varialbe OPENWEATHER_API_KEY is empty.')
    if not key_valid:
        raise InvalidFormat('Invalid API key format.')
    else:
        key = os.environ['OPENWEATHER_API_KEY']

except (EmptyValue, KeyError):
    exit('Undefined environment variable OPENWEATHER_API_KEY.')

except InvalidFormat:
    exit(f'This doesn\'t look like valid API key: {key}')

try:
    city = os.environ['CITY_NAME']
    if len(city) == 0:
        raise EmptyValue('Environment varialbe CITY_NAME is empty.')
except KeyError:
    exit('Undefined environment variable CITY_NAME.')

try:
    api_call        = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key
    api_response    = requests.get(api_call)
    if api_response.status_code != 200:
        raise ApiError(api_response.status_code)
    else:
        response_json   = api_response.json()
        response_city   = response_json['name']
        response_desc   = response_json['weather'][0]['description']
        response_temp   = response_json['main']['temp']
        response_hmdt   = response_json['main']['humidity']
        print(f'source=openweathermap, city="{response_city}", description="{response_desc}", temp={response_temp}, humidity={response_hmdt}')
except ApiError:
    exit(f'API call ended with status code {api_response.status_code}: {api_response.reason}')