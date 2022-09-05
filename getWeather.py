import requests #The module in python that allows us to send requests to API


API_KEY = "" # need to get API key from openweathermap
BASE_URL ="http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
# We have the base url and we are passing the API key, API key is they query parameter. 
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" #Final query parameter is city and we are going to be looking for the data associated with the city. In other words the query is the city. 
response = requests.get(request_url) #We are using the http "get" request to the request url and we are receiving the response.

if response.status_code == 200: #Status code 200 = successful, checking to see if the call was successful.
    data = response.json()# We get the data back as a JSON object, so it needs to be converted into a python dictionary.
    weather = data["weather"][0]["description"]#Targeting the data that we want from the dictionary.
    
    temperature = data["main"]["temp"]#Targeted the temp from the dictionary.
    fahrenheitTemp = round(1.8*(temperature-273) + 32) #turned the weather from kelvin to fahrenheit
   #I had to round to a whole number since it gave me a really long decimal. 

    print("Weather: ", weather)
    print("Temperature is: ", fahrenheitTemp, "degrees Fahrenheit")
else:
        print("An error occurred.") #If not successful
