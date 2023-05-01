import re
url = "https://www.amazon.in/LG-Inverter-Direct-Cool-Refrigerator-GL-B221ASCY/dp/B084XYB5KS?SubscriptionId=AKIAJPUIEK6464M5F3DQ&tag=toda07-21&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B084XYB5KS,LG"

# extract the ASIN from the URL
#asin = url.split("/")[4].split("?")[0]

asin_regex = r"/dp/([A-Z0-9]{10})"

# search the URL using the regular expression
match = re.search(asin_regex, url)

# extract the ASIN from the match
asin = match.group(1)

print(asin)  # output: B0B25DFS8K
