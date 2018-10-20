#Let's start by importing Pandas
import pandas as pd
import csv

#Next, we set the path:
voting_data = "Resources/election_data.csv"
#Now we just have to read the file
voting_data_pd= pd.read_csv(voting_data)

#Now call the header of the data file to make sure we have the right one

print(voting_data_pd.head())

#Let's move on to the assignment:

# -The total number of votes cast

#We'll find this by finding the length of the data since each data point is a vote
TotalVotes = len(voting_data_pd)
print ("Total Number of votes: "+ str(TotalVotes))

# -A complete list of candidates who received votes

# I think we can solve this just by using the unique function. 
# It should show each unique candidate who received votes

uniqueCandidates = voting_data_pd["Candidate"].unique()
print("Candidate: " + uniqueCandidates)

# -The total number of votes each candidate won
# We'll just use the count function to get the total number of votes

Totalcount = voting_data_pd["Candidate"].value_counts()
print("The total count is: " + str(Totalcount))

# -The percentage of votes each candidate won

#There are two ways I've figured how to do this.
#The first way is to get the individual count of each candidate
Khancount = voting_data_pd['Candidate'].tolist().count("Khan")
Correycount = voting_data_pd['Candidate'].tolist().count("Correy")
Licount = voting_data_pd['Candidate'].tolist().count("Li")
OTooleycount = voting_data_pd['Candidate'].tolist().count("O'Tooley")

#let's test to make sure we're getting the individual counts
print(OTooleycount)

print(Khancount)

# Then we define a function to help us get the percent
# To get percentage let's take the 'count' and divide by the 'total votes'

def percent(part,whole):
    return 100 * int(part)/int(whole)
Khanpercent = percent(Khancount, TotalVotes)
print("Khan percent of votes: " + str(Khanpercent)+" %")
Correypercent = percent(Correycount, TotalVotes)
print("Correy percent of votes: "+ str(Correypercent)+" %")
Lipercent = percent(Licount, TotalVotes)
print("Li percent of votes: " + str(Lipercent)+" %")
OTooleypercent = percent(OTooleycount, TotalVotes)
print("O'Tooley percent of votes: " + str(OTooleypercent)+" %")

#Alternative method for percentage
count = voting_data_pd["Candidate"].value_counts('Khan')
count*100

# -The winner of the election based on popular vote.
winner = Totalcount.max()

if winner == Khancount:
    print("Khan wins! " + str(winner) + " votes")
if winner == Correycount:
    print("Correy wins! " + str(winner) + " votes")
if winner == Licount: 
    print("Li wins! " + str(winner) + " votes")
if winner == OTooleycount: 
    print("O'Tooley wins! " + str(winner) + " votes")

#Now we need to export the file:
VotingText = open("PollResults.txt","w+")
VotingText.write("Final Analysis: \r\n")
VotingText.write("----------------------------\r\n")
VotingText.write("Total Number of votes: "+ str(TotalVotes) + "\r\n")
VotingText.write("Candidates: " + str(uniqueCandidates)+ "\r\n")
VotingText.write("---------------------\r\n")
VotingText.write("The total count is: " + "\r\n" + str(Totalcount) + "\r\n")
VotingText.write("----------------\r\n")
VotingText.write("Khan percent of votes: " + str(Khanpercent)+" %" + "\r\n")
VotingText.write("Correy percent of votes: " + str(Correypercent)+" %" + "\r\n")
VotingText.write("Li percent of votes: " + str(Lipercent) + " %" + "\r\n")
VotingText.write("O'Tooley percent of votes: " + str(OTooleypercent) + " %" + "\r\n")
VotingText.write("-------------------------------\r\n")
if winner == Khancount:
    VotingText.write("Khan wins! " + str(winner) + " votes" + "\r\n")
if winner == Correycount:
    VotingText.write("Correy wins! " + str(winner) + " votes" + "\r\n")
if winner == Licount: 
    VotingText.write("Li wins! " + str(winner) + " votes" + "\r\n")
if winner == OTooleycount: 
    VotingText.write("O'Tooley wins! " + str(winner) + " votes" + "\r\n")
VotingText.close()
