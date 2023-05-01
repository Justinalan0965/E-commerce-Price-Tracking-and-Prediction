import pandas as pd
import re

def identify_website(url):
  
    amazon_regex = r"^(https?://)?(www\.)?amazon\.[a-z]{2,3}(/\S*)?$"
    flipkart_regex = r"^(https?://)?(www\.)?flipkart\.com(/\S*)?$"

    if re.match(amazon_regex, url):
        return "Amazon"
    elif re.match(flipkart_regex, url):
        return "Flipkart"
    else:
        print("Unknown")



with open("test.csv") as file:
    df = pd.read_csv(file)
    row = df['URL']
    print(row[3])
    print(len(df))
for i in range(len(df)):
    url = str(row[i])
    if identify_website(url) == "Flipkart":   
        pid = url.split("pid=")[1].split("&")[0]
        df['URL'] = row.replace(to_replace= url, value=pid)
        row = df['URL']
        print(df)
    elif identify_website(url) == "Amazon":
        asin_regex = r"/dp/([A-Z0-9]{10})"
        match = re.search(asin_regex, url)
        asin = match.group(1)
        df['URL'] = row.replace(to_replace= url, value=asin)
        row = df['URL']
        print(df)
df.to_csv("testing.csv",index=False)

