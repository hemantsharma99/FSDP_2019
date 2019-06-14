# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:39:28 2019

@author: admin
"""

import sqlite3
from pandas import DataFrame
conn=sqlite3.connect("University.db")
c=conn.cursor()
c.execute ("""CREATE TABLE university(
          Name TEXT,
          Age INTEGER,
          Roll_No INTEGER,
          Banch INTEGER
          )""")
c.execute("INSERT INTO university VALUES ('Hemant Sharma', '20','60','CSE')")
c.execute("INSERT INTO university VALUES ('Himanshu Garg', '20','61','CSE')")
c.execute("INSERT INTO university VALUES ('Ankush Pokharna', '20','24','CSE')")
c.execute("INSERT INTO university VALUES ('Ashutosh Bansal', '20','30','CSE')")
c.execute("INSERT INTO university VALUES ('Ayush Gupta', '20','32','CSE')")
c.execute("INSERT INTO university VALUES ('Divyansh Devda', '20','48','CSE')")
c.execute("INSERT INTO university VALUES ('Dilip Kumar', '20','46','CSE')")
c.execute("INSERT INTO university VALUES ('Deepak Sharma', '20','40','CSE')")
c.execute("INSERT INTO university VALUES ('Garvit Agarwal', '20','50','CSE')")
c.execute("INSERT INTO university VALUES ('Deepanshy Choudhary', '42','60','CSE')")
c.execute("SELECT * FROM university")
df=DataFrame(c.fetchall())
df.columns=["Name","Age","Roll_No","Branch"]
conn.commit()
conn.close()