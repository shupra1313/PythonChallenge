import os
import csv
from pathlib import Path

filepath = Path("PyPoll","election_data.csv")
# Declare variables
#Totalvotes_cast = 
#percentage_votes = 
#Totalvotes_won = 

# Open file linked to the path
with open(filepath, newline="") as csvfile:
    # Read files
    csvreader = csv.reader(csvfile, delimiter=',')
    # Loop through all the datas we collect 
    for row in csvfile:
        print(row)




# Printing required final output
#Print("Election Results" )
#print(------------------------------)
#print("Total Votes:"  )
#print(------------------------------)
#print("Winner:"   )
