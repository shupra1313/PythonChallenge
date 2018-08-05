# Importing dependency modules for os,csv & path
import os
import csv
from pathlib import Path

# Link file path to Python
filepath = ("C:\\Users\\Subha\\repos\\python-challenge\\PyBank\\budget_data.csv")
#Initialize variables to empty lists
month_list = []
revenue = []
avgchange = []
# open file which is linked from the path 
with open(filepath, encoding='utf-8') as csvfile:
    # Read files
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skips the headers of the csv file
    next(csvreader,None)
    # Loop through all the datas we collect 
    for row in csvreader:
        #print(row)
        # add total no. of months for the entire period
        # Calculate net amount over entire period
        revenue.append(int(row[1]))   
        month_list.append(row[0])
    
    for i in range(1,len(revenue)):
        avgchange.append(revenue[i] - revenue[i-1])
    
    max_change = max(avgchange)
    max_index = avgchange.index(max_change)
    #print(max_index)
    greatest_month = month_list[max_index + 1]
    #print(greatest_month)
    min_change = min(avgchange)
    min_index = avgchange.index(min_change)
    #print(min_index)
    least_month = month_list[min_index+1]
    #print(least_month)

    print("Financial Analysis\n")
    print("----------------------------------\n")
    print("Total Months:" + str(len(month_list)) + '\n')
    print("Total: $" + str(sum(revenue)) + '\n')
    print("Average Change: " + str("$") + str(sum(avgchange)/(len(month_list)-1) + '\n')
    print("Greatest Increase in Profits: " + str(greatest_month) + str("$") + str(max_index) + '\n')
    print("Greatest Decrease in Profits: " + str(least_month) + str("$"(min_index)))


#"
filepath_1 = ("C:\\Users\\Subha\\repos\\python-challenge\\PyBank\\output_pybank.txt")
# opens the output destination in write mode and prints the summary
with open(filepath_1, 'w') as writefile:
    csvwriter = csv.writer(writefile, delimiter=",")
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(len(month_list)) + '\n')
    writefile.writelines('Total: $' + str(sum(revenue)) + '\n')
    writefile.writelines('Average Change: ' + str('$') + str(sum(avgchange)/(len(month_list)-1)) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + str(greatest_month) +  str('$') + str(max_index) + '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + str(least_month) + str('$') + str(min_index))

#opens the output file in r mode and prints to terminal
with open(output, 'r') as readfile:
    print(readfile.read())





