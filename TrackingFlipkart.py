import pandas as pd
import bs4
import csv
import urllib.request

datas = {}

data_csv = 'E-commerce-Price-Tracking-and-Prediction\product_data.csv'


def flip(url):

    url = url

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    x = soup.find('span',class_="B_NuCI").text
    y = soup.find('div',class_="_30jeq3 _16Jk6d").text.replace(",","").replace("₹","")

    print(x)
    print("\n"+y)

    datas.update({'URL':url})
    datas.update({'product':x})
    datas.update({'price':float(y)})
    
    print(datas)
    #storing data into the csv file
    df = pd.DataFrame([datas])
    print(df)
    
    with open(data_csv,'r') as csvfile:
        csv_dict = [row for row in csv.DictReader(csvfile)]
        if len(csv_dict) == 0:
            print("The file is empty")
            df.to_csv(data_csv,index=False)
        else:
            print("The file is not empty")
            df.to_csv(data_csv,mode='a',index=False,header=False)
            


def list():

    with open(data_csv) as csvfile:
        reader = csv.DictReader(csvfile)

        product_name = []
        product_price = []
        product_url = []
        for row in reader:
            product_url.append(row['URL'])
            product_name.append(row['product'])
            product_price.append(row['price'])

        return product_name,product_price,product_url
    
def trackprice(url,count):

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    y = soup.find('div',class_="_30jeq3 _16Jk6d").text.replace(",","").replace("₹","")

    current_price = float(y)

    print(current_price)

    ddf = pd.read_csv('E-commerce-Price-Tracking-and-Prediction\product_data.csv')

    
    if count < len(ddf):
        stored_price = ddf['price'].iloc[count]
        print("storedPrice:" ,stored_price)
        if current_price < stored_price:
            string = "The price has droped\n"
            Difference = stored_price - current_price
            return string,Difference
        else:
            string = "There is no price change"
            Difference = 0.0
            return string,Difference
    else:
        return "there seems to be an error in the csv file"


def county(counter):
     return counter+1

def realTracker():
    counter = 0

    with open(data_csv) as data:
        data = csv.DictReader(data)
        for url in data:
            print(url['URL']) 

            counter = county(counter)

            string,difference = trackprice(url['URL'],counter-1)

            print(string,difference)







def clear(product_data):
    file1 = open(product_data,'w+')
    file1.close()




#clear(data_csv)

# url = input("Paste your URL: ")

# datas.update({'URL':url})

#flip(url)

# realTracker()


# list()

