# Description
Python script that prints current weather using Open Weather api

# Usage
```
python3 -m pyenv env
source env/bin/activate
pip3 install -r requirements.txt
declare -x OPENWEATHER_API_KEY=XXX
declare -x CITY_NAME=Honolulu
python3 get_weather.py
```

# Sample Output
```
source=openweathermap, city="Honolulu", description="broken clouds", temp=294.92, humidity=77
```
