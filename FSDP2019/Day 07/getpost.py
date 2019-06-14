# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:58:41 2019

@author: admin
"""

import json
import requests
Host="http://13.127.155.43/api_v0.1/sending"
Data={"Phone_Number":"9521988291","Name":"Hemant","College_Name":"PCE","Branch":"CSE"}
headers = {"Content-Type":"application/json","Content-Length":len(Data),"data":json.dumps(Data)}
def post_method():
    response = requests.post(Host,Data,headers)
    return response
print ( post_method().text )
def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving?Phone_Number=9521988291")
    return response
print (get_method().text)