# def IDCount(ID):
#     return ID+1

# def jip():
#     ID = 0

#     ID = IDCount(ID)
#     print(ID)
# for i in range(5):
#     jip()


# index = 0
# def func():
#     global index
#     index+=1
# for i in range(5):
#     func()
#     print(index)


# import pandas as pd
# import bs4
# import csv
# import urllib.request

# datas={}
data_csv = "E-commerce-Price-Tracking-and-Prediction\\test.csv"
# ID = 0

# def flip(url):
#     global ID

#     url = url
#     ID+=1
#     print(ID)

#     sauce = urllib.request.urlopen(url).read()
#     soup = bs4.BeautifulSoup(sauce,"html.parser")

#     x = soup.find('span',class_="B_NuCI").text
#     y = soup.find('div',class_="_30jeq3 _16Jk6d").text.replace(",","").replace("₹","")

#     print(x)
#     print("\n"+y)

#     datas.update({'productID':ID})
#     datas.update({'product':x})
#     datas.update({'URL':url})
#     datas.update({'price':float(y)})
    
#     print(datas)

#     #storing data into the csv file
#     df = pd.DataFrame([datas])
#     print(df)
    
#     with open(data_csv,'r') as csvfile:
#         csv_dict = [row for row in csv.DictReader(csvfile)]
#         if len(csv_dict) == 0:
#             print("The file is empty")
#             df.to_csv(data_csv,index=False)
#         else:
#             print("The file is not empty")
#             df.to_csv(data_csv,mode='a',index=False,header=False)



# for i in range(5):
#     url = input("Paste the link here: ")
#     flip(url)
#     print("added to the csv") 



# importing the pandas library
# import pandas as pd

# # reading the csv file
# df = pd.read_csv(data_csv)

# print(len(df))
# # updating the column value/data
# for i in range(1,len(df)+1):
#     n = int(i)
#     print(n)
#     df.loc[i-1, 'productID'] = n

# # writing into the file
# df.to_csv(data_csv, index=False)

# print(df)
