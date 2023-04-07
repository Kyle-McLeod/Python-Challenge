#import dependencies
import os
import csv

#access CSV data
poll_csv = os.path.join("Resources", "election_data.csv")

#set up variables
total_votes = 0
cand1_votes = 0
cand2_votes = 0
cand3_votes = 0
cand1_percent = 0
cand2_percent = 0
cand3_percent = 0
runners = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
winner = []

#open CSV as a dictionary
with open(poll_csv) as poll_data:
     
   poll_dreader = csv.DictReader(poll_data)

#for loop to add up the vote values, then count the votes cast to each specific candidate
   for line in (poll_dreader):

        total_votes = total_votes +1

        if str(line["Candidate"]) == (runners[0]):
            cand1_votes = int(cand1_votes) + 1

        elif str(line["Candidate"]) == (runners[1]):
            cand2_votes = int(cand2_votes) + 1

        elif str(line["Candidate"]) == (runners[2]):
            cand3_votes = int(cand3_votes) + 1

#if statement to find out which candidate received the most votes
if cand1_votes >= cand2_votes | cand3_votes:
    winner.append(runners[0])

elif cand2_votes >= cand1_votes | cand3_votes:
    winner.append(runners[1])
    
elif cand3_votes >= cand1_votes | cand3_votes:
    winner.append(runners[2])

#calculate the number of votes against the total to find the percentage
cand1_percent = (cand1_votes / total_votes) * 100
cand1_percent = round(cand1_percent, 3)
cand2_percent = (cand2_votes / total_votes) * 100
cand2_percent = round(cand2_percent, 3)
cand3_percent = (cand3_votes / total_votes) * 100
cand3_percent = round(cand3_percent, 3)

#print results to terminal
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------------")
print(f"{runners[0]}: {cand1_percent}% ({cand1_votes})")
print(f"{runners[1]}: {cand2_percent}% ({cand2_votes})")
print(f"{runners[2]}: {cand3_percent}% ({cand3_votes})")
print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

#print results to .txt file (code looks roung, but spaces make the final output look cleaner)
with open('election_results.txt', 'w') as f:
    f.write(f'Election Results,  --------------------       Total Votes: {total_votes},  --------------------     {runners[0]}: {cand1_percent}% ({cand1_votes}),     --------------------         {runners[1]}:           {cand2_percent}% ({cand2_votes}),     --------------------      {runners[2]}:           {cand3_percent}% ({cand3_votes}),     --------------------      Winner: {winner}')

