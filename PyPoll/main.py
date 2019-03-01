import pandas as pd

# Create dataframe with .csv election data
df = pd.read_csv('election_data.csv')

# Get the total number of votes cast
total_votes = len(df.index)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

# Get a list of all candidates
candidate_list = list(set(df['Candidate'].tolist()))

# Establish "winner" variables
winner = ""
winning_votes = 0

# Iterate through and print desired output
for candidate in candidate_list:
    num_votes = len(df[df['Candidate'] == candidate].index)
    if num_votes > winning_votes:
        winner = candidate
    print(str(candidate) + ": " +
          str("{:.3f}".format(num_votes/total_votes * 100)) +
          "% (" + str(num_votes) + ")")

    
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")
