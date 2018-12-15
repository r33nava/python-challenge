# -*- coding: utf-8 -*-
"""
Author: Reena Desai

Python Homework: PyPoll

Description: In this challenge, I am tasked with helping a small, rural town 
modernize its vote-counting process. 

I will be given a set of poll data called election_data.csv. 
The dataset is composed of three columns: Voter ID, County, and Candidate. 

My task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.

"""

#Dependencies
import csv


#Create empty lists sets for candidates, vote list and total votes
candidatelist = []
votelist = []
total_votes = []

#Open CSV file
with open('election_data.csv') as election_data:
  csvreader = csv.reader(election_data)

    for row in csvreader:

       votelist.append(row[0])
       candidatelist.append(row[0])


# Counts the list of votes per candidate 

candidates = list(set(candidatelist))

for x in candidates:
    total_votes.append(candidatelist.count(x))


# Export to textfile 
file = ("output.txt","w")
with open(file) as txtfile:
    file.write("Election Results")
    file.write("----------------------")
    file.write("Total Votes:" + total_votes)
    file.write("----------------------")
    


#Print Results
print("Election Results")
print("----------------------")
print("Total Votes: " + total_votes)
print("----------------------")
  