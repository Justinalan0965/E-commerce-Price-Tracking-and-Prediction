
import csv

testcsv = "E-commerce-Price-Tracking-and-Prediction\\test.csv"

def untracking(ids):
    lines = list()

    members= str(ids)
    #input("Enter the ID: ")
    #input("Please enter a member's name to be deleted.")
    print("\n")
    print(members)
    print("\n")
    print(type(members))

    with open(testcsv, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)


            for field in row:

                if field == members:

                    print("match found")

                    lines.remove(row)
                    lines = [x for x in lines if x != []]


    with open(testcsv, 'w',newline="") as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)

untracking(6)