# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Define the path to the csv file
csvpath = os.path.join("/Users/josefinadesolminihac/Desktop/Bootcamp/Challenges/python-challenge/PyBank/Resources/budget_data.csv")

#Create a list for storage the number of months
month = []
#Create a list for storage the sum of Profit and Loses
total_profit_losses = []
#Create a list for storage the changes in Profit/Losses
list_changes_profit_losses= []

change_profit_losses=0



# Read in the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header row first
    csv_header = next(csvfile)
    #Read each row of data after the header
    for row in csvreader:
    #For every row add to the list month the element in row 0
       month.append(row[0])
       num_month =len(month)
    #For every row add the profit or loss to the total_profit_losses list
       total_profit_losses.append(int(row[1]))
       total = sum(total_profit_losses)
    #Calculate the changes in "Profit/Losses" over the entire period.
    for i in range (len(total_profit_losses)-1):
        change_profit_losses = total_profit_losses[i+1] - total_profit_losses[i]
        list_changes_profit_losses.append(change_profit_losses)
        #Calculate the average of the changes in "Profit/Losses" over the entire period.
        average_change = round(sum(list_changes_profit_losses)/len(list_changes_profit_losses),2)
        
    #Calculate the greatest increase in profits (date and amount) over the entire period
    increased= max(list_changes_profit_losses)
    #Identify the date of the greatest increase in profits.
    index_month_increased = list_changes_profit_losses.index(increased)+1
    month_increased = month[index_month_increased]
    #Calculate the greatest decrease in profits (date and amount) over the entire period
    decreased= min(list_changes_profit_losses)
    #Identify the date of the greatest decrease in profits.
    index_month_decreased = list_changes_profit_losses.index(decreased)+1
    month_decreased = month[index_month_decreased]

    

#Present the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_month}")
print(f"Total: $ {total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increased in Profits: {month_increased} (${increased})")
print(f"Greatest Decreased in Profits: {month_decreased} (${decreased})")

#Export a text file with the results
results = open("results_pybank.txt", "w")
results.write("Financial Analysis \n")
results.write("---------------------------- \n")
results.write(f"Total Months: {num_month} \n")
results.write(f"Total: ${total} \n")
results.write(f"Average Change: ${average_change} \n")
results.write(f"Greatest Increased in Profits: {month_increased} (${increased}) \n")
results.write(f"Greatest Decreased in Profits: {month_decreased} (${decreased}) \n")   