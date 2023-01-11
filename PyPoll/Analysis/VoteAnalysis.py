# importing required libraries
import os
import csv
import collections

# declaring necessary variables
votesTotal = 0
candidates = []
votesCandidate1 = 0
votesCandidate2 = 0
votesCandidate3 = 0
votesPercentage = []
winner = ""

# creating a collection of votes
votes = collections.Counter()

# setting the cross platform csv path
csvPath = os.path.join("..", "Resources", "election_data.csv")

# initiating the file handler
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # storing the header
    csvHeader = next(csvReader)

    for row in csvReader:
        votesTotal += 1

        # counting votes
        votes[row[2]] += 1

        # creating list with all candidates
        if row[2] not in candidates:
            candidates.append(row[2])

# storing votes per candidate
votesCandidate1 = votes['Charles Casper Stockham']
votesPercentage.append((votesCandidate1 / votesTotal) * 100)
votesCandidate2 = votes['Diana DeGette']
votesPercentage.append((votesCandidate2 / votesTotal) * 100)
votesCandidate3 = votes['Raymon Anthony Doane']
votesPercentage.append((votesCandidate3 / votesTotal) * 100)

# determining the winner
if votesCandidate1 > votesCandidate2:
    winner = candidates[0]
elif votesCandidate2 > votesCandidate3:
    winner = candidates[1]
else:
    winner = candidates[2]


# printing results on terminal
print(f"Election Results")
print(f"--------------------------")
print(f"Total votes: {votesTotal}")
print(f"--------------------------")
print(
    f"Charles Casper Stockham: {votesPercentage[0]:.2f}% ({votesCandidate1})")
print(f"Diana DeGette: {votesPercentage[1]:.2f}% ({votesCandidate2})")
print(f"Raymon Anthony Doane: {votesPercentage[2]:.2f}% ({votesCandidate3})")
print(f"--------------------------")
print(f"Winner: {winner}")

# printing results on txt file
with open("analysis.txt", 'w') as txtFile:
    print(f"Election Results", file=txtFile)
    print(f"--------------------------", file=txtFile)
    print(f"Total votes: {votesTotal}", file=txtFile)
    print(f"--------------------------", file=txtFile)
    print(
        f"Charles Casper Stockham: {votesPercentage[0]:.2f}% ({votesCandidate1})", file=txtFile)
    print(
        f"Diana DeGette: {votesPercentage[1]:.2f}% ({votesCandidate2})", file=txtFile)
    print(
        f"Raymon Anthony Doane: {votesPercentage[2]:.2f}% ({votesCandidate3})", file=txtFile)
    print(f"--------------------------", file=txtFile)
    print(f"Winner: {winner}", file=txtFile)
txtFile.close()
