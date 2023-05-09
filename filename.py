import csv
import re

testcsv = "testing.csv"

def getFilename2(ids):
    lines = list()

    members= str(ids)
    with open(testcsv, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    print("match found")
                    print(row[1])
                    return(row[1])
                
def identify_website(url):
  
    amazon_regex = r"^(https?://)?(www\.)?amazon\.[a-z]{2,3}(/\S*)?$"
    flipkart_regex = r"^(https?://)?(www\.)?flipkart\.com(/\S*)?$"

    if re.match(amazon_regex, url):
        return "Amazon"
    elif re.match(flipkart_regex, url):
        return "Flipkart"
    else:
        print("Unknown")


def getFilename(url):

    if identify_website(url) == "Flipkart":   
            pid = url.split("pid=")[1].split("&")[0]

    elif identify_website(url) == "Amazon":
            asin_regex = r"/dp/([A-Z0-9]{10})"
            match = re.search(asin_regex, url)
            pid = match.group(1)


    file_name = getFilename2(pid)

    return file_name