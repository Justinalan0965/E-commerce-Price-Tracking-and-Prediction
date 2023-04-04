import requests
import pandas as pd
from bs4 import BeautifulSoup

# Dataset = {"Names": [], "Prices": [], "RAM|ROM": [], "Camera": [],
#            "Display": [], "Processor": [], "Battery": [], "Ratings": []}
NoneElement = BeautifulSoup("<p>None</p>", 'html.parser')

# for i in range(1, 49):
#     url = "https://www.flipkart.com/search?q=mobiles+above+30000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles+above+30000%7CMobiles&requestId=3400d73b-ede5-45b3-beef-26b97e78a7ce&as-searchtext=mobile+above+30&p%5B%5D=facets.price_range.from%3D30000&p%5B%5D=facets.price_range.to%3DMax&page=" + \
#         str(i)

url = "https://www.flipkart.com/asus-vivobook-k15-oled-2022-ryzen-5-hexa-core-amd-r5-5500u-8-gb-1-tb-hdd-256-gb-ssd-windows-11-home-km513ua-l502ws-thin-light-laptop/p/itmbe79f1096e453?pid=COMG87FFPDWUZAKE&lid=LSTCOMG87FFPDWUZAKEIKWIHF&marketplace=FLIPKART&q=asus+hybrid+laptop&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=08695369-e89c-4118-8c2d-272482ed1d76.COMG87FFPDWUZAKE.SEARCH&ppt=sp&ppn=sp&ssid=iypssl0qw00000001680425443302&qH=596218d17264b41a"

s = requests.get(url)

soup = BeautifulSoup(s.text, "html.parser")
main = soup.find("div", class_="_1YokD2 _3Mn1Gg")

names = main.find_all("div", class_="_4rR01T")
prices = main.find_all("div", class_="_30jeq3 _1_WHN1")
desc = main.find_all("ul", class_="_1xgFaf")
ratings = main.find_all("div", class_="_3LWZlK")


print(names)
print(prices)

    # Shadowing unexisted props
#     if len(prices) != len(names):
#         for i in range(len(prices), len(names), 1):
#             prices.append(NoneElement)
#     if len(ratings) != len(names):
#         for i in range(len(ratings), len(names), 1):
#             ratings.append(NoneElement)
#     if len(desc) != len(names):
#         for i in range(len(desc), len(names), 1):
#             desc.append(NoneElement)

#     for i in desc:
#         d = i.find_all('li', class_="rgWa7D")
#         if len(d) >= 5:
#             Dataset["RAM|ROM"].append(str(d[0].text.strip()))
#             Dataset["Display"].append(str(d[1].text.strip()))
#             Dataset["Camera"].append(str(d[2].text.strip()))
#             Dataset["Battery"].append(str(d[3].text.strip()))
#             Dataset["Processor"].append(str(d[4].text.strip()))
#         else:
#             Dataset["RAM|ROM"].append(NoneElement)
#             Dataset["Display"].append(NoneElement)
#             Dataset["Camera"].append(NoneElement)
#             Dataset["Battery"].append(NoneElement)
#             Dataset["Processor"].append(NoneElement)

#     for i in names:
#         n = i.text
#         Dataset["Names"].append(str(n))

#     for i in prices:
#         p = i.text
#         Dataset["Prices"].append(p)

#     for i in ratings:
#         r = i.text
#         Dataset["Ratings"].append(r)

# df = pd.DataFrame.from_dict(Dataset)
# print(df)
# df.to_csv("GT30K.csv", header=True, index=False)
# print("Saved sucessfully!")

# next_page = soup.find("a", class_="_1LKTO3").get("href")
# comp_page = "https://www.flipkart.com" + next_page
# print(comp_page)