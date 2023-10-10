#Current Weather API
#Using coordinates from Geocode API

def getCurrentWeather(lat,lon):

    #import pprint
    import requests

    #API KEY
    APIkey = '3e5358db3b3ab858d99d68405fe62b0b'

    # BASE URL with API KEY
    #apicall = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={APIkey}'
    
    #Geocoding API
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={APIkey}'
    
    try:
        # Send an HTTP GET request to the specified URL with optional headers
        response = requests.get(url)

        # Check the response status code to see if the request was successful (HTTP 200 OK)
        if response.status_code == 200:
            # If the request was successful, print the response content (JSON data)
            print("Response Content for current Weather API:")
            #Convert response to JSON Object for manipulation
            jsonResponse = response.json()
            
            #Retrives desired weather data; temperature, city, weather description, 
            temp = jsonResponse['main']['temp']
            city = jsonResponse['name']
            description = jsonResponse['weather'][0]['description'].title() #The title() method capitalizes the first letter of each word in the string while converting the rest of the characters to lowercase.
            icon = jsonResponse['weather'][0]['icon']
            
            #Retrieve Icon URL by using image path instead of API
            iconURL = f'https://openweathermap.org/img/wn/{icon}@2x.png'
            
            return temp, city, description, iconURL
                        
        else:
            # If the request was not successful, print an error message with the status code
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"An error occurred: {e}")
        
#print(getCurrentWeather())