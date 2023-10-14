
def getVerse():

    #import pprint

    import random

    import requests
    from bs4 import BeautifulSoup
    
    dailyVerseList = ['JER.29.11',
                  'ROM.12.2',
                  'PHP.4.6',
                  'PHP.4.13',
                  'MAT.6.33',
                  'MAT.11.28',
                  'ISA.54.17',
                  'DEU.31.6',
                  '2CO.5.7',
                  'JOS.1.9',
                  'ISA.41.10',
                  'MRK.10.27',
                  'PRO.3.5']
    
    randomDailyVerse = random.choice(dailyVerseList)
    
    #import json
    #from html2json import collect
    #Get All Books with their Id
    #url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books"
    # Define the URL you want to send the GET request to
    #url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/PRO/chapters"
    # Get All verses in Chapter
    #url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/PRO.5/verses"
    # Get All verses in Chapter
    url = f"https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/verses/{randomDailyVerse}"

    # Define any additional headers you might need (optional)
    headers = {
        "api-key": "49f329b4538a0d4405bbe12eb94cbd6d"  # Add your API key if required
    }
    
    try:
        # Send an HTTP GET request to the specified URL with optional headers
        response = requests.get(url, headers=headers)

        # Check the response status code to see if the request was successful (HTTP 200 OK)
        if response.status_code == 200:
            # If the request was successful, print the response content (JSON data)
            print("Response Content:")
            #Convert response to JSON Object for manipulation
            jsonResponse = response.json()
            
            #print(jsonResponse)
            chapter = jsonResponse['data']['reference']
            verseHtmlObject = jsonResponse['data']['content']
            
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(verseHtmlObject, 'html.parser')

            # Find all <p> tags and extract their text
            p_tag = soup.find('p',class_='p')

            # Extract and print the modified text from each <p> tag
            text = p_tag.get_text()
            
            # Find the index of the first non-numeric character
            index = next((i for i, c in enumerate(text) if not c.isdigit()), None)

            # Remove the leading numbers if they exist
            if index is not None:
                text = text[index:]
            else:
                text = text  # No leading numbers found

            # Print the modified string
            #print(text)
            
            return chapter,text
                        
        else:
            # If the request was not successful, print an error message with the status code
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"An error occurred: {e}")
       
getVerse()