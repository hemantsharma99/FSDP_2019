# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:13:28 2019

@author: admin
"""

import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)
response = requests.get(url)
response.content
print(type(response.content))
jsondata=response.json()
print(jsondata)
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
print("Longitude>"+str(jsondata['coord']['lon']))
print("Lattitude>"+str(jsondata['coord']['lat']))
print("Weather Condition>"+jsondata['weather'][0]['main'])
print("Wind Speed>"+str(jsondata['wind']['speed']))
print("Sunrise>"+str(jsondata['sys']['sunrise']))
print("Sunset>"+str(jsondata['sys']['sunrise']))