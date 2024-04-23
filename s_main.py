import numpy as np
import pandas as pd
import time
from selenium import webdriver
import os.path
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#You can download the necessary driver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads
#Note down the path to the driver.exe
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
count = 0
#"Travelers", "Walgreens Boots Alliance", "Dow", "3M", "American Express", "Goldman Sachs", "Caterpillar",
#             "IBM", "Boeing", "Amgen", "Honeywell", "McDonald’s", "Chevron", "Cisco"
companies = ["Salesforce", "Coca-Cola", "Merck & Co.", "Nike", "Intel", "Verizon", "Home Depot", "Disney"
            "Procter & Gamble", "UnitedHealth Group", "Walmart", "Johnson & Johnson", "JPMorgan Chase",
            "Visa", "Microsoft", "Apple"]


columns = ["company_name", "Number of jobs about AI", "location", "summary"] #column names
#Creates the columns to store my information using panda
sample_df = pd.DataFrame(columns=columns)

#creates a loop that grabs the desirable infromation from each comapny.
for x in companies:
    count = count + 1
    # paste the website you want to scrap
    driver.get("https://www.indeed.com/jobs?q=artificial+intelligence+company%3A" + x + "&l=")
    # The try-catch exception is for the case there are 0 results
    try:
        numOfResult = driver.find_element_by_id('searchCountPages').text
    except NoSuchElementException:
        numOfResult = "No Result"
    sample = [] #creates a temporary list
    sample.append(driver.title) #adds in the title of the page in the first row
    sample.append(numOfResult) #adds in the number of job posting for second column
    sample.append("Santa Barbara") #hard coded santa barara for third column
    sample.append("something askdfkdjas lkfa") #hard coded for fourth column
    #time delay of 7 secs before the enxt request, to not overwhelm the server
    time.sleep(7)
    sample_df.loc[count] = sample #inserts the row

driver.close() #closes the tab after the for loop finishes

##Saves the sample in a csv: notes, csv must be closed before this runs.(Overwrites anything else you have)
#sample_df.to_csv("C:\Expriment\Sample.csv", encoding='utf-8')

## This if statement is for appending to existing document instead of overwriting it.
if(os.path.isfile("C:\Expriment\Sample.csv")):
    sample_df.to_csv("C:\Expriment\Sample.csv", mode='a', header=False, encoding='utf-8')
else:
   sample_df.to_csv("C:\Expriment\Sample.csv", encoding='utf-8')
