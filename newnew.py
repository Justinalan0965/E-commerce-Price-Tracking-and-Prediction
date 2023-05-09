# import pandas as pd
# import bs4
# import csv
# import urllib.request

# product_data = "rawdata.csv"

# datas = {}
# fieldnames = ['product','price']



# def flip(url):
#     sauce = urllib.request.urlopen(url).read()
#     soup = bs4.BeautifulSoup(sauce,"html.parser")

#     x = soup.find('span',class_="B_NuCI").text
#     y = soup.find('div',class_="_30jeq3 _16Jk6d").text.replace(",","").replace("₹","")

#     # print(x)
#     # print("\n"+y)

#     datas.update({"product":x})
#     datas.update({"price":float(y)})

#     #print(datas)

    
#     with open('rawdata.csv', 'w') as file:
#         writer = csv.DictWriter(file,fieldnames=fieldnames)
#         writer.writerow(datas)
#         writer.writeheader(fieldnames)

#     print("checking for price drops...")
#     current_price = float(y)
#     stored_price =float(datas["price"])

#     if current_price < stored_price:
#         changeprice = stored_price - current_price
#         print("price dropped")
#         print(changeprice)
#         return changeprice
    
#     else:
#         print("no price dropped")
#         return "Price is unchanged"

# def amazon(url):
#     #creating a variable    
#     sauce = urllib.request.urlopen(url).read()

#     # convert it into a beautiful soup object
#     soup = bs4.BeautifulSoup(sauce,"html.parser")
#     dataname = soup.find('span',{'id':'productTitle'}).text.strip()
#     datars = soup.select_one("span.a-price-whole").text.replace(",","")

#     # print(dataname)
#     # print(eval(datars)) 

# e_com = input("Enter your ecommerce website:")

# if e_com == "amazon":
#     url = input("enter amz link:")
#     amazon(url)

# elif e_com == "flip":
#     url = input("enter Flip link:")
#     flip(url) 

# else:
#     print("no ecomm web found")



def a():
    global size
    size = "61,999.00"

def b():
    newsize = size.replace(",","").replace("₹","")
    return newsize

a()
bn = float(b())
print(type(bn))