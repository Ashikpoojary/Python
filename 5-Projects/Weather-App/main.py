# requests library is a powerful and user-friendly tool for making HTTP requests, 
# allowing you to easily interact with web services and APIs.
import requests
import json

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=13c21fb6489c46bfa7a192917250708&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
print('Temperature:',wdic["current"]["temp_c"])