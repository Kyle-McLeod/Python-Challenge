#import dependencies
import os
import csv

#access CSV data
csvpath = os.path.join("Resources", "budget_data.csv")

#setup variables
total_months = 0
total_profit_loss = 0
profit_loss = 0
avg_pl = 0
monthly_change = 0
monthly_change_list = []
prev_value = 0
month = []

#open CSV as dictionary
with open(csvpath) as budget_data:
     
   budget_dreader = csv.DictReader(budget_data)
#for loop tocount the number of months and profit in the dataset
   for line in (budget_dreader):
      total_months = total_months + 1
      total_profit_loss = total_profit_loss + int(line["Profit/Losses"])
#calculate the month to month change in the profit/loss value     
      monthly_change = int(line["Profit/Losses"]) - prev_value
      prev_value = int(line["Profit/Losses"])
      monthly_change_list = monthly_change_list + [monthly_change]
      
#calculate the average monthly change
average_change = sum(monthly_change_list) / len(monthly_change_list)

#sort the list in ascending order to determine the greatest increase and decrease, then round the the hundreth place
monthly_change_list.sort()
trunc_average_change = round(average_change, 2)

#print results to terminal
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_months)
print("Total:", total_profit_loss)
print("Average Change:", trunc_average_change)
print("Greatest Increase in Profits:", monthly_change_list[-1])
print("Greatest Decrease in Profits:", monthly_change_list[0])

#print results to .txt file (code looks rough, but it keeps the outut looking clean)
with open('financial_analysis.txt', 'w') as f:
    f.write(f"Financial Analysis  --------------------        Total Months: {total_months}           Total: {total_profit_loss}           Average Change: {trunc_average_change} Greatest Increase in Profits: {monthly_change_list[-1]}                Greatest Decrease in Profits: {monthly_change_list[0]}")


        
        
        
        
        
        
        
        
 
        













        













