import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import sklearn.metrics as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection  import train_test_split
from filename import *

# Load the dataset
def getThelink(url,lastprice):
    id = url
    file_name = getFilename(id)
    fname = "dataset/"+str(file_name)
    df = pd.read_csv(fname)
    l = len(df)

    # with open(fname, "r", encoding="utf-8", errors="ignore") as scraped:
    #         final_line = scraped.readlines()[-1]
    #         last = final_line.split(',')
    # print(last)

    print(type(lastprice))
    actual_price = float(lastprice)

    # Split the dataset into features and target variable
    X = df.drop("price", axis=1)
    y = df["price"]
    model = LinearRegression()

    x_train,x_test,y_train,y_test = train_test_split (X,y,test_size=0.20)
    #model.fit(X,y)

    model.fit(x_train,y_train)
    print(model.score(x_train,y_train))
    y_pred=model.predict(x_test)
    print("R2 score: ",round(sm.r2_score(y_test,y_pred),2))

    x= l +30
    p = pd.array([x]).reshape(-1,1)
    pred_price = model.predict(p)[0]
    pred_price = int(pred_price)
    print("Predicted price: ",pred_price)
    price = str(pred_price)[-1:] 
    price = float(price)
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
         ret_string = "<i>The price drop chances are..</i>"+str(percent)+"%"
         return pred_price,ret_string


    elif actual_price < pred_price:
         pricedrop = pred_price-actual_price
         pricedrop_percent = (pricedrop/actual_price)*100
         percent = round(pricedrop_percent,2)
         ret_string = "<i>The price might increase by..</i>"+str(percent)+"%"
         return pred_price,ret_string

    else:
        return 0,"The price drop chances are nearly 0"