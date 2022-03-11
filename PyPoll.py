# Modules
import os
import csv

# The data we need to retrieve
# Open the election results and read the file.
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:
     # To do: perform analysis.
     file_reader = csv.reader(election_data)
     # Print the header row.
     headers = next(file_reader)
     print(headers)
     # for row in file_reader:
     #    print(row)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Close the file
outfile.close()

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Close the file.