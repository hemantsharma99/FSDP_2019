# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:49:20 2019

@author: admin
"""
from bs4 import BeautifulSoup
import requests
import sqlite3
from pandas import DataFrame
source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print(source)
soup = BeautifulSoup(source,"lxml")
print (soup.prettify())
right_table=soup.find('table', class_='table')
print (right_table.prettify())
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
conn = sqlite3.connect('odi_ranking.db')
c=conn.cursor()
c.execute ("""CREATE TABLE odi(
          POS INTEGER,
          Team  TEXT,
          Points INTEGER,
          Weighted_Matches INTEGER,
          Rating INTEGER
          )""")
for i in range(0,len(A)):
    c.execute("INSERT INTO odi VALUES ('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))
c.execute("SELECT * FROM odi")
df = DataFrame(c.fetchall())
df.columns = ["POS","Team","Points","Weighted_Matches","Rating"]
conn.commit()