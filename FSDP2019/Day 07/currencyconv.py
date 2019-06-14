# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:39:19 2019

@author: admin
"""

import requests
url=" http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=79d8c21829bb751d1ad1"
response=requests.get(url,)
jsondata=response.json()
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
print("Conversion price>"+" "+str(jsondata['USD_INR']))
