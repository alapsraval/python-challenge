
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called [election_data.csv]. 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

  # The total number of votes cast

  # A complete list of candidates who received votes

  # The percentage of votes each candidate won

  # The total number of votes each candidate won

  # The winner of the election based on popular vote.
    
import os
import csv
import statistics 

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip Header
    csv_header = next(csv_reader)
    
    # The total number of votes cast
    total_votes = 0
    # A complete list of candidates who received votes
    candidates = dict()
    winner = ''
    
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
    # The winner of the election based on popular vote.        
    winner = max(candidates.items(), key=lambda x : x[1])

    #Print results

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    for candidate, votes in candidates.items():
        print(f"{candidate}: {round(votes*100/total_votes,3)}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner[0]}")
    print("-------------------------")
    
    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    with open('results.txt', 'w') as output_file: 
        output_file.write("Election Results\n-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            output_file.write(f"{candidate}: {round(votes*100/total_votes,3)}% ({votes})\n")
        output_file.write("-------------------------\n")    
        output_file.write(f"Winner: {winner[0]}\n")
        output_file.write("-------------------------")    
