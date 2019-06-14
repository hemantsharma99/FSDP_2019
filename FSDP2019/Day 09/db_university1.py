# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:54:16 2019

@author: admin
"""

import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://hemantsharma99:unpredictable@hemant-8qdei.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb = client.yourdbname
def add_details(Name, Age, Roll_No, Branch):
    mydb.Hemant.Sharma.insert_one({"Name" :Name,"Age" : Age,"Roll_No" : Roll_No,"Branch" : Branch})
    return "Details added successfully"
def fetch_all_details():
    user = mydb.Hemant.Sharma.find()
    for i in user:
        print (i)
add_details('Hemant Sharma', '20','60','CSE')
add_details('Himanshu Garg', '20','61','CSE')
add_details('Ankush Pokharna', '20','24','CSE')
add_details('Ashutosh Bansal', '20','30','CSE')
add_details('Ayush Gupta', '20','32','CSE')
add_details('Divyansh Devda', '20','48','CSE')
add_details('Dilip Kumar', '20','46','CSE')
add_details('Deepak Sharma', '20','40','CSE')
add_details('Garvit Agarwal', '20','50','CSE')
add_details('Deepanshy Choudhary', '42','60','CSE')
fetch_all_details()