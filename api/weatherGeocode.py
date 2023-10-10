#Retrieve Geocoding API for coordinates parameter for Current Weather API

def getWeatherGeoCode():

    import json

    import requests

    #API KEY
    APIkey = '3e5358db3b3ab858d99d68405fe62b0b'
    
    #Zip Code
    zip_code = '95008'
    
    #Country Code
    country_code = 'US'
    
    # BASE URL with API KEY
    #apicall = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={APIkey}'
    
    #Geocoding API
    url = f'https://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={APIkey}'
    
    # API RESPONSE
    
    
    
    try:
        # Send an HTTP GET request to the specified URL with optional headers
        response = requests.get(url)

        # Check the response status code to see if the request was successful (HTTP 200 OK)
        if response.status_code == 200:
            # If the request was successful, print the response content (JSON data)
            #print("Response Content:")
            #Convert response to JSON Object for manipulation
            jsonResponse = response.json()
            #print(jsonResponse)
            #Retrieve latitude and longitude coordinates
            lat = jsonResponse['lat']
            lon = jsonResponse['lon']
            
            return lat,lon
                        
        else:
            # If the request was not successful, print an error message with the status code
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"An error occurred: {e}")
        
#print(getWeatherGeoCode())