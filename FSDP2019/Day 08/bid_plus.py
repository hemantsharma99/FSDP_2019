# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:13:48 2019

@author: admin
"""

import pandas as pd
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://bidplus.gem.gov.in/bidlists")
for i in range(1,11):
    print(i)
    right_table=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    print(right_table.text)
    right_table1=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/strong')
    right_table2=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/strong')
    right_table3=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[1]/strong')
    right_table4=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/strong')
    right_table5=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/strong')


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a