# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee requested the following data:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate received
4. The total number of votes each candidate received
5. The winner of the election
6. The percentage of the total votes from each county
7. The total number of votes from each county
8. The county with the largest turnout

This data is printed to the terminal and to a text file.
## Resources
- Data Source: election_results.csv
- Python, Visual Studio Code

## Election-Audit Results
The analysis of the election shows that: 
- 369,711 votes were cast in this election
- The candidates that received votes were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote, 85,213 total votes
  - Diana DeGette received 73.8% of the vote, 272,892 total votes
  - Raymon Anthony Doane received 3.1% of the vote, 11,606 total votes
- The winner of the election was Diana DeGette, who received 73.8% of the vote, 272,892 total votes
- The counties that cast votes were:
  - Jefferson with 10.5% of votes cast, a total of 38,855 votes
  - Denver with 82.8% of votes cast, a total of 306,055 votes
  - Arapahoe with 6.7% of votes cast, a total of 24,801 votes
 - The county with the most votes cast was Denver with 82.8% of votes cast, a total of 306,055 votes

## Election-Audit Summary
The script can be used to analyze results in a csv file that is formatted the same as election_results.csv (ballot #, county, candidate). By changing the file_to_load variable, the script can reference a different data source. Alternatively, file_to_load can be changed to an input value and the file can be determined at runtime. The file_to_save variable can be changed, to print t a different file and not continually overwrite the analysis each time.
