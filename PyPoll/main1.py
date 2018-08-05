import csv
import os
from pathlib import Path

#set path
filepath = Path("C:\\Users\\Subha\\repos\\python-challenge\\PyPoll\\election_data.csv")
#open the file
with open(filepath, newline="",encoding='utf-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   #Initialize variables to empty lists and dictionary
   total_votes = 0
   candidates = []
   candidates_dict = {}
   #winning_votes = []
   next(csvreader)
   #go line by line and process each vote
   for row in csvreader:
       # add to total number of votes
       total_votes += 1
       if row[2] not in candidates:
           #add candidates to the empty list
           candidates.append(row[2])
           #to make candidate name as the key
           candidates_dict[row[2]] = 0
           candidates_dict[row[2]] = candidates_dict[row[2]] + 1
    

   print('Election Results\n')
   print('---------------------------\n')
   print("Total Votes: " + str(total_votes) + '\n')
   print('----------------------------\n')
   print(str(candidates_dict) + '\n')
   print('----------------------------\n')
   #print("Winner: ")
   print('----------------------------\n')

#open new file
#new_file = open("output_PyPoll.txt", "w")

# writing the new file
#new_file.write("Election Results \n")
#new_file.write("------------------------------------- \n")
#new_file.write("Total Votes: " + str(total_votes) + "\n")
#new_file.write("------------------------------------- \n")
#for candidates in candidates_dict:
    #votes = candidates_dict.get(candidates)
    #percentage = votes / total_votes
    #new_file.write(candidates + ':' + str(round(percentage,2)*100) + ' : (' + str(votes) + ')''\n')
    #if votes > winning_votes:
        #winning_votes = votes
        #winner = candidates
#new_file.write("------------------------------------- \n")        
#new_file.write('Winner is: ' + winner + ' (' + str(winning_votes) + ')''\n')
   
   #closing of file
#new_file.close()

#sets path for output file
#filepath = os.path.join('raw_data',file_name)
#output = os.path.join("Output_PyPoll", "output.txt")
# opens the output destination in write mode and prints the summary
#with open(output, 'w') as writefile:
    #writefile.writelines('Election Results\n')
    #writefile.writelines('------------------------------\n')
    #writefile.writelines('Total Votes: ' + str(total_votes) + '\n')
    #writefile.writelines('------------------------------\n')
    #writefile.writelines(str(candidates_dict) + '\n')
    #writefile.writelines('----------------------------\n')
    #writefile.writelines("Winner: ")
    #writefile.writelines('----------------------------\n')

#opens the output file in r mode and prints to terminal
#with open(output, 'r') as readfile:
    #print(readfile.read())