# importing required libraries
import os
import csv

# declaring necessary variables
rowNumber = []
rowName = []
rowsList = []
increase = []
totalRows = 0
totalIncrease = []
rowTotal = 0
averageChange = 0
greatestIncrease = 0
increaseMonth = ""
greatestDecrease = 0
decreaseMonth = ""

# setting the cross platform csv path
csvPath = os.path.join("..", "Resources", "budget_data.csv")

# initiating the file handler
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # storing the header
    csvHeader = next(csvReader)

    # looping throught the file to read and count data
    for row in csvReader:
        rowTotal = rowTotal + int(row[1])
        rowsList.append(row)
        rowName.append(row[0])
        rowNumber.append(row[1])
totalRows = len(rowNumber)

# calculating total, increase, decrease and average change
for i in range(len(rowsList)):
    increase = int(rowNumber[i]) - int(rowNumber[i-1])
    totalIncrease.append(increase)
greatestDecrease = min(totalIncrease)
greatestIncrease = max(totalIncrease)
averageChange = (sum(totalIncrease)/totalRows)

# parsing the month name
for i in range(len(rowsList)):
    if int(rowsList[i][1]) == greatestDecrease:
        decreaseMonth = rowsList[i]
    elif int(rowsList[i][1]) == greatestIncrease:
        increaseMonth = rowsList[i]

# printing results on terminal
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {totalRows}')
print('Total: $' + str(rowTotal))
print(f'Average Change: $ {averageChange:.2f}')
print('Greatest Increase in Profits: ' +
      increaseMonth + '($' + str(greatestIncrease) + ")")
print('Greatest Decrease in Profits: ' +
      decreaseMonth + '($' + str(greatestDecrease) + ")")

# printing results on txt file
with open("analysis.txt", 'w') as txtFile:
    print('Financial Analysis', file=txtFile)
    print('-------------------------', file=txtFile)
    print(f'Total Months: {totalRows}', file=txtFile)
    print('Total: $' + str(rowTotal), file=txtFile)
    print(f'Average Change: $ {averageChange:.2f}', file=txtFile)
    print('Greatest Increase in Profits: ' +
          increaseMonth + '($' + str(greatestIncrease) + ")", file=txtFile)
    print('Greatest Decrease in Profits: ' +
          decreaseMonth + '($' + str(greatestDecrease) + ")", file=txtFile)
txtFile.close()
