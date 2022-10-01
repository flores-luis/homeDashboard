import datetime as dt
import requests as req

dateobject = dt.datetime.now()

dayOfWeek = dateobject.strftime("%A")
timeOfDay = dateobject.strftime("%I:%M %p")
currentDate = dateobject.strftime("%B %d, %Y")

wkey = 'd534761adfab2cf209e9c9916d82717a'
stateISO_code = 'CA'
countryISO_code = 'US'

cityInput = input("Enter a city in California?")
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={cityInput},{stateISO_code},{countryISO_code}&appid={wkey}"

#Using a GET request to retrieve data
GetRequestWebPage = req.get(BASE_URL)
#Request Code result
codeResult = GetRequestWebPage.status_code

#Converting data requested to json format or turns a dictionary???
#d = data into dictionary
d = GetRequestWebPage.json()
#print(d)
#print(type(d))

if d['weather'][0]['main'] == err:
    print(f"Request code of {codeResult}")
    print("This is an error with the user's input")
    exit()
else:
    print("Program is working succesfully")

#print(d.keys())
currentWeather = d['weather'][0]['main']
currentWeatherDescription = d['weather'][0]['description']
current_kelvinWeather = d['main']['temp']
#converting Kelvin weather data to Ferenahit
currentWeatherDegrees = int(round(1.8*(current_kelvinWeather-273) + 32))

print(f"The current weather is {currentWeather} with some {currentWeatherDescription} and current temperature is {currentWeatherDegrees}°F")
print(f"Today is {dayOfWeek} {currentDate}\nThe time is {timeOfDay}")
