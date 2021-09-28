# load csv 
import csv

# open file
with open('/Users/johnhope/Desktop/DS3002/AMZN.csv') as csvDataFile:
# read file as csv
    csvReader = csv.reader(csvDataFile)
  
# print row by row
    for row in csvReader:
        print(row)
