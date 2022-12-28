# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Define the path to the csv file
csvpath = os.path.join("/Users/josefinadesolminihac/Desktop/Bootcamp/Challenges/python-challenge/PyPoll/Resources/election_data.csv")
#Define that total of votes starts in 0.
total_votes= 0
#Start the count of votes in 0
votes_stockham = 0
votes_degette = 0
votes_doane = 0

# Read in the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header row first
    csv_header = next(csvfile)
    #Read each row of data after the header
    for row in csvreader:
        #Calculate the total number of votes cast
        total_votes += 1
        #Define where is the candidate name
        candidate_name = row[2]
    #Sum the votes for the 3 candidates
        if candidate_name == "Charles Casper Stockham":
            votes_stockham = votes_stockham + 1
        elif candidate_name == "Diana DeGette":
            votes_degette = votes_degette + 1
        else:
            votes_doane = votes_doane + 1
    #Calculate the percentage of each candidate
    percentage_stockham = votes_stockham/total_votes *100
    percentage_degette = votes_degette/total_votes*100
    percentage_doane = votes_doane/total_votes*100
      
#Determine the winner
#List of votes 
votes = {"Charles Casper Stockham" : votes_stockham, "Diana DeGette": votes_degette, "Raymon Anthony Doane": votes_doane}
winner = max(votes, key=votes.get)


#Results for each candidate

#Print analysis results
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}\n")
print("-----------------------------")
print(f"Charles Casper Stockham: {percentage_stockham:.2f}% ({votes_stockham})")
print(f"Diana DeGette: {percentage_degette:.2f}% ({votes_degette})")
print(f"Raymon Anthony Doane: {percentage_doane:.2f}% ({votes_doane})")
print("-----------------------------")
print(f"Winner: {winner} ")
print("-----------------------------")

#Export a text file with the results
results_pypoll = open("results_pypoll.txt", "w")
results_pypoll.write("Election Results \n")
results_pypoll.write("---------------------------- \n")
results_pypoll.write(f"Total Votes: {total_votes} \n")
results_pypoll.write("---------------------------- \n")
results_pypoll.write(f"Charles Casper Stockham: {percentage_stockham:.2f}% ({votes_stockham}) \n")
results_pypoll.write(f"Diana DeGette: {percentage_degette:.2f}% ({votes_degette}) \n")
results_pypoll.write(f"Raymon Anthony Doane: {percentage_doane:.2f}% ({votes_doane}) \n")
results_pypoll.write("---------------------------- \n")
results_pypoll.write(f"Winner: {winner} \n")
results_pypoll.write("---------------------------- \n")