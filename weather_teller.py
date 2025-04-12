import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


api='http://api.weatherapi.com/v1/current.json?key=e9d039e99cba413e977130023251004&q=London&aqi=no'
city=input('Enter city name : ')
url=f'http://api.weatherapi.com/v1/current.json?key=e9d039e99cba413e977130023251004&q={city}&aqi=no'
r=requests.get(url)
try:
    response = requests.get(url)
    response.raise_for_status()
    wdic = response.json()

    # Extract useful info
    temp = wdic['current']['temp_c']
    feels = wdic['current']['feelslike_c']
    condition = wdic['current']['condition']['text']
    wind_kph = wdic['current']['wind_kph']
    wind_dir = wdic['current']['wind_dir']
    humidity = wdic['current']['humidity']
    pressure = wdic['current']['pressure_mb']
    visibility = wdic['current']['vis_km']
    uv = wdic['current']['uv']
    rain = wdic['current']['precip_mm']
    cloud = wdic['current']['cloud']

    sp = (
        f"Here's the weather update for {city}. "
        f"The temperature is {temp} degrees Celsius, feels like {feels}. "
        f"Condition is {condition}. "
        f"Wind is blowing at {wind_kph} kilometers per hour from {wind_dir}. "
        f"Humidity is {humidity} percent. "
        f"Visibility is {visibility} kilometers. "
        f"Pressure is {pressure} millibars. "
        f"UV index is {uv}. "
        f"Rainfall is {rain} millimeters. "
        f"Cloud cover is at {cloud} percent."
    )

except Exception as e:
    sp = "City not found or there was an error fetching the weather data. Please try another city."
    print("Error:", e)

if __name__ == '__main__':
    print(sp)
    speak(sp)
