# importing required libraries
import os
import csv

# declaring necessary variables
rowNumber = 0
rowTotal = 0
averageCharge = 0
greatestIncrease = 0
increaseMonth = " "
greatestDecrease = 0
decreaseMonth = " "

# setting the cross platform csv path
csvPath = os.path.join("..", "Resources", "budget_data.csv")

# initiating the file handler
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # storing the header
    csvHeader = next(csvReader)

    # looping throught the file to read and count data
    for row in csvReader:
        rowNumber += 1
        rowTotal = rowTotal + int(row[1])
        averageCharge = rowTotal / rowNumber  # incorrect
        if int(row[1]) > int(greatestIncrease):
            increaseMonth = row[0]
            greatestIncrease = row[1]

        if int(row[1]) < int(greatestDecrease):
            decreaseMonth = row[0]
            greatestDecrease = row[1]

    # printing results on terminal
    print('Financial Analysis')
    print('-------------------------')
    print('Total Months: ' + str(rowNumber))
    print('Total: $' + str(rowTotal))
    print('Average Change: $' + str(averageCharge))
    print('Greatest Increase in Profits: ' +
          increaseMonth + '($' + str(greatestIncrease) + ")")
    print('Greatest Decrease in Profits: ' +
          decreaseMonth + '($' + str(greatestDecrease) + ")")

# printing results on txt file
with open("analysis.txt", 'w') as txtFile:
    print('Financial Analysis', file=txtFile)
    print('-------------------------', file=txtFile)
    print('Total Months: ' + str(rowNumber), file=txtFile)
    print('Total: $' + str(rowTotal), file=txtFile)
    print('Average Change: $' + str(averageCharge), file=txtFile)
    print('Greatest Increase in Profits: ' +
          increaseMonth + '($' + str(greatestIncrease) + ")", file=txtFile)
    print('Greatest Decrease in Profits: ' +
          decreaseMonth + '($' + str(greatestDecrease) + ")", file=txtFile)
txtFile.close()
