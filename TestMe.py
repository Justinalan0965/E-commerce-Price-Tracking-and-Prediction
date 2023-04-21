
import csv

testcsv = "E-commerce-Price-Tracking-and-Prediction\\test.csv"


lines = list()

members= input("Please enter a member's name to be deleted.")

with open(testcsv, 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if field == members:

                lines.remove(row)
                lines = [x for x in lines if x != []]

with open(testcsv, 'w',newline="") as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)