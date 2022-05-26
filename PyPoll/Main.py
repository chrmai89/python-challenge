import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
file_output = "analysis/PyPoll_analysis.txt"

#variables
total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(csv_header)

    for x in csvreader:

        #Count total votes
        total_votes = total_votes + 1

        #Candidate name from each row
        candidate_name = x["Candidate"]

        if candidate_name not in candidates:
            candidates.append(candidate_name) #Add list of candidate to list

            #Add each candidates vote count
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


            for y in candidate_votes:

                # Vote count and percentage
                votes = candidate_votes.get(y)
                vote_percentage = float(votes) / float(total_votes) * 100

                # Winning vote count and candidate
                if (votes > winning_count):
                    winning_count = votes
                    winning_candidate = y          
            
with open(file_output, "w") as txt_file:

    # Print final results
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{y}: {vote_percentage: .3f}% ({votes})\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(election_results)

#Print results to external file
with open(file_output, "w") as txt_file:
    txt_file.write(election_results)