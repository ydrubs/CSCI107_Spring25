"""
Example 1
This shows how to use the request library to make an API call.
The dictionary API does not require an access key.
We can read the responce text into a variable. The responce text is a string.
"""
# import requests # import the request library to allow us to 'ask' a URL for data
#
# word = input("Enter a word: ") # Allow user to enter a word for lookup
#
# # api_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'.format(word=word) #call the API url formatted with the word user provided
# api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}' # ...We can also use f-strings
#
# response = requests.get(api_url)  #Make the request and get the response code from the server
# print(response)
#
# if  response.status_code == requests.codes.ok: #If response is ok (200), print the data returned
#     print(response.text)
#     print(type(response.text))

"""Example 2
In this example we import the JSON library. 
JSON is a database structure that is designed to be readable by both humans and machines.

We use JSON to turn the response into a list. This makes it easier to get the data we needed from the response results
"""
import requests # import requests
import json # Import JSON library

word = input("Enter a word: ")
api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
responce = requests.get(api_url)
if responce.status_code == requests.codes.ok:
    json_data = json.loads(responce.text) #Use JSON to convert data to a Python list

# Some exploratory printing/debugging
print(json_data)
print(type(json_data))

data =  dict(json_data[0]) #Convert to a dictionary
print(data)

inner_data = data['meanings'][0]
print(inner_data)

definition = inner_data['definitions'][0]
print(definition['definition'])

# By examing the dictionary we see a number of dictionaries, embedded in lists, embedded in dictionaries
# We have to try to unpack this to get to the 'definition' key/index
# print(data)


# pass #We access the meanings key and the first value for that key ('definitions)
# print(inner_data)

# We notice that the 'inner data' is another dictionary whose keys are a list, we try to print the first element to verify.
# print(pass)


pass #We only want the definition key which is the first part of definition
pass #Here it is!!


"""Example 3
In the following set of examples, we use natural gas data from thr U.S. energy administration.
We can access the data, restructure it to make it more readable then process the data to answer certain questions"""


# pass # This library let't you open URL requests with Python (alternative to above method)
# import json

# api_url = 'https://pkgstore.datahub.io/core/natural-gas/monthly_json/data/dbd6262f71e7c30614c2d6eb4dfcfb72/monthly_json.json'
# url_result = urlopen(api_url)
# print(url_result) #HTTP responce as an object. We can break it up into method calls as needed
# raw_data = url_result.read() #Read the data as a raw JSON string (not Python string)
# print(raw_data)
# json_data = json.loads(raw_data) #Convert to a Python list (as above)
# print(json_data)

pass # Look through the data in a more structured way to see its structure.


## We can access individual elements in the list of dictionaries
## In this case we are printing the month of the first available data point
## print(pass)


"""
Let's make this more readable by converting to lists of tuples
We can use enumerate to index elements that are directly accessed with the loop
"""
## Build a Tuple list of (month, price)
pass

## Now we can do some data processesing
## Lets first find the average price of natural gas over the time in the data
# x = sum(n for _,n in json_data) #Use list comprehension (actually a generator) to find the sum of the second element (price)
# print(x/len(json_data)) #Calculate and print the average

#Let's find the highest and lowest prices in the data
# print(max((p,m) for m,p in json_data)) # max() only looks at the first element of the tuple, so we flip the elements to compare
# print(min((p,m) for m,p in json_data))


# #Let's pull out all data points where price is greater then 10
# #in this case, we populate a new list (x), with data that has the second element greater then 10.
# high_prices = [(m,p) for m,p in json_data if p > 10]
# print(high_prices)

# Sort from highest to lowest price
# print(sorted(((p,m) for m, p in high_prices), reverse=True))


"""
Example 4
In the following example, we use the APIninja website to request and parse a quote using an API key.
We can copy/paste and modify the example on the website to suit our application: https://api-ninjas.com/api/quotes
Reminder: You need an account first to recieve your API key
"""

# import requests
# import json

###################
## CATEGORY is now a PAID option
# category = 'happiness' #From the documentation we see we can (optionally) specifiy a category
# api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
###################


# api_url = 'https://api.api-ninjas.com/v1/quotes'
# headers = {'X-Api-Key': 'XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR'} # We need to send an API key in the form of headers

# response = pass #Replace with YOUR OWN API key (XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR)


"""
To help structure our program better, every time data is returned, 
the function below is used to pull out the text of the quote alone.
"""
pass
#      #convert to list
#
#
#      #Get the dictionary representation
#
#
#      #Pull out the value for the key equal to 'quote'
#
#
#      # send data back form the function


# if response.status_code == requests.codes.ok:
#     pass #As long as the response is valid call the function to off-load the processing
# #
# else:
#     pass  # ...or if an error occurs, return error code



"""
Example 5
NASA's APOD (Astronomy picture of the day) API: https://api.nasa.gov/
Since the NASA API does not need headers, we can use a generic request (rather then calling GET), with a 'GET' parameter. 
This returns dictionary data
We can then get the image URL and open it from a browser
"""
# import requests
# import json
## We will open a web browser to show the image. We can also design a GUI with Tkinter or another library to display the image there instead.
pass

# url = 'https://api.nasa.gov/planetary/apod'
# api_key = 'ubWfZS1xbjvdqAjBjyLrTcbFe0KLO3DVkqwuMb2s' #Replace with ubWfZS1xbjvdqAjBjyLrTcbFe0KLO3DVkqwuMb2s to run
# date = pass
# querystring = pass


""" 
Call the request and turn it into a Python useable format
In the previous examples, we directly called the 'get' request through a method. 
Here, we specifiy the type of request when making the API call.
"""

pass
pass # turn it into json
pass #Note: this response is already in the dict data-type


"""
After examining the data in the response and understanding its type, we want to pull out the image linked in the response and display it.
"""
pass


"""
If the URL is an image (vs a video) then open it in a browser.
We could also skip this check and open the associated media in a browser regardless of type.
However, for future code, could help seperating out how images and videos are handled
"""
pass
