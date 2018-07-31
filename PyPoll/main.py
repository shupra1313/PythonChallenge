import os
import csv
import math
from pathlib import Path

filepath = Path("C:\\Users\\Subha\\repos\\python-challenge\\PyPoll\\election_data.csv")
# Declare variables
votes = 0
candidates = {}

#Totalvotes_won = 

# Open file linked to the path
with open(filepath, newline="") as csvfile:
    # Read files
    csvreader = csv.reader(csvfile, delimiter=' ')
    next(csvreader)
    # Loop through all the datas we collect 
    for row in csvreader:
        #print(row)
        votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    print (candidates)
        #if candidates(row[2])
    print(votes)

# Printing required final output
#Print("Election Results" )
#print(------------------------------)
#print("Total Votes:"  )
#print(------------------------------)
#print("Winner:"   )
