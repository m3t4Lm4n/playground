import os
import pyowm
import re

class EmptyValue(Exception):
    pass
class InvalidFormat(Exception):
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

owm = pyowm.OWM(key)
if owm.is_API_online() == True:
    observation = owm.weather_at_place(city)
    location    = observation.get_location().get_name()
    weather     = observation.get_weather()
    description = weather.get_detailed_status()
    temperature = weather.get_temperature()['temp']
    humidity    = weather.get_humidity()
    print(f'source=openweathermap, city="{city}", description="{description}", temp={temperature}, humidity={humidity}')
else:
    exit('API not online.')