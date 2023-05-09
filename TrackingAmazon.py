import pandas as pd
import bs4
import csv
import urllib.request

datas = {}

data_csv = 'amazon_data.csv'

ID = 0

def amazon(url):

    global ID
    url = url
    ID+=1

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    x = soup.find('span',{'id':'productTitle'}).text.strip()
    y = soup.select_one("span.a-price-whole").text.replace(",","")

    print(x)
    print("\n"+y)

    datas.update({'productID':ID})
    datas.update({'product':x})
    datas.update({'URL':url})
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
        #print(product_name,product_price,product_url)

def amznsize():
    with open(data_csv) as cs:
        readit = csv.DictReader(cs)
        size = []
        for i in readit:
            size.append(i['product'])
    list_size = len(size)
    return list_size
            

def untrackA(ID):

    lists = []

    members= str(ID)
    #members = input("Please enter a member's name to be deleted.")
    print("\n")
    print(members)
    print("\n")
    print(type(members))

    with open(data_csv, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lists.append(row)

            for field in row:
                print(field)
                print(type(field))
                if field == members:

                    print("match found")

                    lists.remove(row)
                    lists = [x for x in lists if x != []]


    with open(data_csv, 'w',newline="") as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lists)
    #updating the productID
    df = pd.read_csv(data_csv)

    print(len(df))
    # updating the column value/data
    for i in range(1,len(df)+1):
        n = int(i)
        print(n)
        df.loc[i-1, 'productID'] = n

    # writing into the file
    df.to_csv(data_csv, index=False)

    print(df)

def trackprice(url,count):

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    y = soup.select_one("span.a-price-whole").text.replace(",","")
    current_price = float(y)

    print(current_price)

    ddf = pd.read_csv('amazon_data.csv')
    
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
# for i in range(10):
#     url = input("Paste your URL: ")
#     amazon(url)

# realTracker()

#list()


#untrackA()


