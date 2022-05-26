import os
import csv
#Variables
month_count = 0
total_Prof_Loss = 0.0
prev_PL = 0
month_change = []
PL_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_PL = 0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
file_output = "analysis/PyBank_analysis.txt"

# Open the CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = csvreader
    #print(csv_header)

    for line in csvreader:
        #totals
        month_count += 1
        total_Prof_Loss += float(line['Profit/Losses'])

        #PL change
        PL_change = float(line['Profit/Losses']) - prev_PL
        prev_PL = float(line["Profit/Losses"])
        PL_change_list = PL_change_list + [PL_change]
        month_change = month_change + [line["Date"]]

        #Greatest increase
        if (PL_change > greatest_increase[1]):
            greatest_increase[0] = line["Date"]
            greatest_increase[1] = PL_change

        #Greatest decrease
        if (PL_change < greatest_decrease[1]):
            greatest_decrease[0] = line["Date"]
            greatest_decrease[1] = PL_change

#Calculate average Profit and Loss change
Profit_Loss_ave = sum(PL_change_list) / len(PL_change_list)
    
        
output = (
    f"\nFinancial Analysis\n"
    f"---------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: {total_Prof_Loss}\n"
    f"Average  Change: $ {Profit_Loss_ave}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})\n")

print(output)

with open(file_output, "w") as txt_file:
    txt_file.write(output)