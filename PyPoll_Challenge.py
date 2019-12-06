# The data we need to retrieve.
# 1. Create a list of counties
# 2. Create a dictionary where county is the key and votes are the values
# 3. Create empty string that wiil hold county name with largest turnout
# 4. Declare a variable that represents the number of votes that a county received
# 5. The winner of the election based on popular vote.

# Add our dependecies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources/election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_results.txt')
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
# 1. Create a list of counties
counties_list = []
# 2. Creat a dictionary
counties_votes ={}
most_votes = 0
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

        # CH. Get the vcounty votes
        county_name = row[1]
        if county_name not in counties_list:
            counties_list.append(county_name)
            counties_votes[county_name] = 0
        counties_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # CH. Iterate through county votes
    for county in counties_votes:
        c_votes = counties_votes[county]
        c_vote_percentage = int(c_votes)/int(total_votes)*100
        county_results = (f"{county}: {c_vote_percentage: .1f}% ({c_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        if (c_votes > most_votes):
            most_votes = c_votes
            largest_turnout = county
    largest_turnout_summary =(
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes)/int(total_votes)*100
        # Print out each candidate's name, vote count, and percentage of 
        # votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and 
            # winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage=vote_percentage
            # Set the winning_candidate equal to the candidate's name. 
            winning_candidate = candidate
    # Print out the winning candidate, vote count and the percentage to terminal.
    winning_candidate_summary =(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
        