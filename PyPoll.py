# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The precentage of votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

Resources/election_results.csv

# Add our dependecies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources/election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candiate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes= {}

# Winning Candidate and Winning Count Tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Addd it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes)/int(total_votes)*100

    # To do: print out each candidate's name, vote count, and percentage of 
    # votes to the terminal.
    print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and 
        # winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage=vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name. 
        winning_candidate = candidate

# To do: print out the winning candidate, vote count and the percentage to terminal.
winning_candidate_summary =(
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}\n"
    f"------------------------\n")
print(winning_candidate_summary)
    