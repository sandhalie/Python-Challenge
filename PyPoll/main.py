import os
import csv

# path to the csv file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #stores the csv header
    csv_header = next(csvreader)
    
    #define the variables
    rowcount  = 0
    candidates =[]
    candidate_votes=[0,0,0]

    for row in csvreader:
        #loop through the data to find the number of rows
        rowcount += 1
        if row[2] not in candidates:
            candidates.append(row[2])

        # the number of votes for each candidate
        if row[2] == candidates[0]:
            candidate_votes[0] +=1
        elif row[2] == candidates[1]:
            candidate_votes[1] +=1
        elif row[2] == candidates[2]:
            candidate_votes[2] +=1  
    
    #format the number of votes into percentages
    percentage = []
    for i in range(0,len(candidate_votes)):
        percentage.append("{:,.3f}%".format(candidate_votes[i]/rowcount*100))
    
    #create the list of text strings that will be printed as the result
    text = []
    text.append(str(f"Election Results"))
    text.append(str(f"----------------------------"))
    text.append(str(f"Total Votes: {rowcount}"))
    text.append(str(f"----------------------------"))
    for i in range(0,len(candidate_votes)):
        text.append(str(f"{candidates[i]}: {percentage[i]} ({candidate_votes[i]})"))
    text.append(str(f"----------------------------"))
    a= candidate_votes.index(max(candidate_votes))
    text.append(str(f"Winner: {candidates[a]}"))
    text.append(str(f"----------------------------"))
    
    #print the analysis
    for row in text:
        print(row)

#path to save text file
textpath = os.path.join("Analysis", "Results.txt")

#write text file
with open(textpath, 'w') as f:
    f.write("\n".join(text))