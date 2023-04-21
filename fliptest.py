from bs4 import BeautifulSoup
import requests
from lxml import etree as et
import random


header_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/103.0.5060.66 Safari/537.36",

              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",

              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]

def get_dom(the_url):
   user_agent = random.choice(header_list)
   header = {"User-Agent": user_agent}
   response = requests.get(the_url, headers=header, stream=True)
   soup = BeautifulSoup(response.text, 'lxml')
   current_dom = et.HTML(str(soup))
   return current_dom



def titleandbrand(dom1):
   try:
       title = dom1.xpath('//span[@class="B_NuCI"]/text()')[0]
   except Exception as e:
       title = 'No title available'
   return title


def salespriceandmrp(dom1):
   try:
       sales_price = dom1.xpath('//div[@class="_30jeq3 _16Jk6d"]/text()')[0].replace(u'\u20B9','')
   except Exception as e:
       sales_price = 'No price available'
   return sales_price

def overallrating(dom1):
   try:
       overall_rating = dom1.xpath('//div[@class="_2d4LTz"]/text()')[0]
   except Exception as e:
       overall_rating = "0"
   return overall_rating

# link = input("Paste your URL: ")  


def scrap_flip(url):

    product_dom = get_dom(url)
    title = titleandbrand(product_dom)
    sales_price = salespriceandmrp(product_dom)
    overall_rating = overallrating(product_dom)



    print(title)
    print("\n")
    print(sales_price)
    print("\n")
    print(overall_rating)
    print("\n")

    return title,sales_price,overall_rating