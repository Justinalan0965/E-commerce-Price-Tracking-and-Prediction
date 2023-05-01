import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from TestMe import *

# Load the dataset
def getThelink(url):
    id = url
    file_name = getFilename(id)
    fname = "dataset/"+str(file_name)
    df = pd.read_csv(fname)
    l = len(df)

    with open(fname, "r", encoding="utf-8", errors="ignore") as scraped:
            final_line = scraped.readlines()[-1]
            last = final_line.split(',')
    print(last)

    actual_price = int(last[1])
    # Split the dataset into features and target variable
    X = df.drop("price", axis=1)
    #X = df['Date']
    y = df["price"]
    model = LinearRegression()
    model.fit(X,y)
    x= l +30
    p = pd.array([x]).reshape(-1,1)
    pred_price = model.predict(p)[0]
    pred_price = int(pred_price)
    print("Predicted price: ",pred_price)
    price = str(pred_price)[-1:] 
    price = int(price)
    #print(price)

    if price < 5:
        newprice = 5-price
        pred_price+=newprice
    elif price > 5:
        newprice = 10-price
        pred_price+=newprice


    print(pred_price)
    print(actual_price)
    if actual_price > pred_price:
         pricedrop = actual_price-pred_price
         pricedrop_percent = (pricedrop/actual_price)*100
         percent = round(pricedrop_percent,2)
         ret_string = "The price drop chances are.."+percent+"%"
         return pred_price,ret_string


    elif actual_price < pred_price:
         pricedrop = pred_price-actual_price
         pricedrop_percent = (pricedrop/actual_price)*100
         percent = round(pricedrop_percent,2)
         ret_string = "The price might increase by.."+percent+"%"
         return pred_price,ret_string

    else:
        return 0,"The price drop chances are nearly 0"