# Data Analysis using Python

A Python project to analyze financial records and a set of poll data.

## PyBank

* A Python script to analyze the [financial records] (PyBank/Resources/budget_data.csv) of a company, composed of two columns: `Date` and `Profit/Losses`.

* It analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* In addition, the script also prints the analysis to the terminal and export a text file with the results.

## PyPoll

* A Python script to help a small, rural town modernize its vote-counting process.

* A set of [poll data] (PyPoll/Resources/election_data.csv), composed of three columns: `Voter ID`, `County`, and `Candidate` is used here. 

* It analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

