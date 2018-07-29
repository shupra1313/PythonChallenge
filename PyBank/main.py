# Importing dependency modules for os,csv & path
import os
import csv
from pathlib import Path

# Link file path to Python
filepath = Path("PyBank","budget_data.csv")
# Declare variables
Total_Months = 0
net_amount = 0
Greatest_Increase = ("" (0))
Greatest_Decrease = ("" (0))
Average_Change = 0
# open file which is linked from the path 
with open(filepath, newline="") as csvfile:
    # Read files
    csvreader = csv.reader(csvfile, delimiter=',')
    # Loop through all the datas we collect 
    for row in csvfile:
        print(row)





#Printing required final output
#print("Financial Analysis")
#print("----------------------------------")
#print("Total Months:"    )
#print("Total Net Amount:"   )
#print("Average Change:"   )
#print("Greatest Increase in Profits:"    )
#print("Greatest Decrease in Profits:"    )