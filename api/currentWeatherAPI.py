#Current Weather API
#Using coordinates from Geocode API

def getCurrentWeather():

    import pprint

    import requests
    from geoCodeAPI import getWeatherGeoCode

    #API KEY
    APIkey = '3e5358db3b3ab858d99d68405fe62b0b'
    
    #Coordinates
    lat,lon = getWeatherGeoCode()
    # print(lat)
    # print(lon)
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
            
            pprint.pprint(jsonResponse,indent=4)
                        
        else:
            # If the request was not successful, print an error message with the status code
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"An error occurred: {e}")
        
print(getCurrentWeather())