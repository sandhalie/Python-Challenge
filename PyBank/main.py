import os
import csv

# path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #stores the csv header
    csv_header = next(csvreader)

    #define the variables
    rowcount  = 0
    profit= []
    month = []

    #loop through data to store month and profit information seperately
    for row in csvreader:
        rowcount += 1
        profit.append(int(row[1]))
        month.append(str(row[0]))

    #calculated the change between months
    change = []
    for i in range(0,len(profit)-1):
        change.append(profit[i+1]-profit[i])

    #format the averae change
    avg_change = "${:,.2f}".format(sum(change)/ len(change))
    
    #define variables
    index_max = change.index(max(change))+1
    index_min = change.index(min(change))+1

    #create the list of text strings that will be printed as the result
    text = []
    text.append(str(f"Financial Analysis"))
    text.append(str(f"----------------------------"))
    text.append(str(f"Total Months: {rowcount}"))
    text.append(str(f"Total : ${sum(profit)}"))
    text.append(str(f"Average Change : {avg_change}"))
    text.append(str(f"Greatest Increase in Profits : {month[index_max]} (${max(change)})"))
    text.append(str(f"Greatest Decrease in Profits : {month[index_min]} (${min(change)})"))
    
    #print the analysis
    for row in text:
        print(row)

#path to save text file
textpath = os.path.join("Analysis", "Results.txt")

#write text file
with open(textpath, 'w') as f:
    f.write("\n".join(text))
