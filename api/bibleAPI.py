
def getVerse():

    #import pprint

    import requests,random
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
            chapterVerseObject = jsonResponse['data']['reference']
            verseHtmlObject = jsonResponse['data']['content']
            
            #print(htmlObjectForVerse)
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(verseHtmlObject, 'html.parser')

            # Find all <p> tags and extract their text
            p_tags = soup.find_all('p')

            #print(p_tags)
            
            sentences = []
            
            # Extract and print the modified text from each <p> tag
            for p_tag in p_tags:
                sentence_parts = p_tag.get_text().split(';')
                for part in sentence_parts:
                    text = ''.join(char for char in part if not char.isdigit())
                    cleaned_text = text.strip()
                    if cleaned_text:  # Check if the sentence is not empty
                        sentences.append(cleaned_text)
                        
            # Use the join() method to combine the sentences into a single string with newline separators
            combined_text = ",\n".join(sentences)
            
            return chapterVerseObject,combined_text
                        
        else:
            # If the request was not successful, print an error message with the status code
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"An error occurred: {e}")