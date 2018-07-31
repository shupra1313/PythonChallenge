# Importing dependency modules for os,csv & path
import os
import csv
from pathlib import Path

# Link file path to Python
filepath = ("C:\\Users\\Subha\\repos\\python-challenge\\PyBank\\budget_data.csv")
# Declare variables
months = 0
revenue = []
avgchange = []
#Greatest_Increase = ("", (0))
#Greatest_Decrease = ("", (0))
# open file which is linked from the path 
with open(filepath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skips the headers of the csv file
    next(csvreader)
   # Read files
    reader_for_csv = csv.reader(csvfile)
    # Loop through all the datas we collect 
    for row in csvreader:
        #print(row)
        # Calculate total no. of months for the entire period
        months += 1 
        # calculate net amount over entire period
        revenue.append(int(row[1]))   
    for i in range(1,len(revenue)):
        avgchange.append(revenue[i] - revenue[i-1])
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months:" + str(months))
    print("Total_net_amount:" + str(sum(revenue)))
    print("Average Change:" + str(sum(avgchange)/(str(months)-1)))