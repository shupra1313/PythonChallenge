import csv
import os
from pathlib import Path

#set path
filepath = Path("C:\\Users\\Subha\\Master Repo\\Working Class Repo\\python-challenge\\PyPoll\\election_data.csv")
print('Election Results\n')
print('---------------------------\n')
#open the file
with open(filepath, newline="",encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Initialize variables to empty lists and dictionary
    votes = []
    total_votes = 0
    candidates = []
    candidates_dict = {}
    winning_votes = 0
    next(csvreader)
    #go line by line and process each vote
    for row in csvreader:
        #add to total number of votes
        total_votes += 1
        if row[2] not in candidates:
            #add candidates to the empty list
            candidates.append(row[2])
        #to make candidate name as the key
            candidates_dict[row[2]] = 0
            candidates_dict[row[2]] = candidates_dict[row[2]] + 1
        else:     
            candidates_dict[row[2]] +=1
    #print(candidates_dict)
    for candidates in candidates_dict:
        votes = candidates_dict.get(candidates)
        percentage = (votes / total_votes)*100
        print(str(candidates) + ':' + str(round(percentage,3)) + ("%") + '   (' + str(votes) + ')' '\n')
        if votes > winning_votes:
            winning_votes = votes
            winner = candidates
            
print("Total Votes: " + str(total_votes) + '\n')
print('----------------------------\n')
print("Winner: " + str(winner) +'\n')
print("Winning Votes: " + str(winning_votes) +'\n')
print('----------------------------\n')

#set path for output file
filepath_1 = ("C:\\Users\\Subha\\Master Repo\\Working Class Repo\\python-challenge\\PyPoll\\output_pypoll.txt")
# opens the output destination in write mode and prints the summary
with open(filepath_1, 'w+') as writefile:
    csvwriter = csv.writer(writefile, delimiter=",")
    writefile.writelines('Election Results\n')
    writefile.writelines('----------------------------\n')
    for candidates in candidates_dict:
        votes = candidates_dict.get(candidates)
        percentage = (votes / total_votes)*100
        writefile.writelines(str(candidates) + ':' + str(round(percentage,3)) + ("%") + '   (' + str(votes) + ')' '\n')
    writefile.writelines("Total Votes: " + str(total_votes) + '\n')
    writefile.writelines('----------------------------\n')
    writefile.writelines("Winner: " + str(winner) +'\n')
    writefile.writelines("Winning Votes: " + str(winning_votes) +'\n')
    writefile.writelines('----------------------------\n')