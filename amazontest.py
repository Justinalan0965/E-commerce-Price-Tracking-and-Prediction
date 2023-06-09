from bs4 import BeautifulSoup
import requests
import random

# Function to extract Product Title
def get_title(soup):
 
 try:
  # Outer Tag Object
  title = soup.find("span", attrs={"id":'productTitle'})

  # Inner NavigableString Object
  title_value = title.string

  # Title as a string value
  title_string = title_value.strip()

 except AttributeError:
  title_string = "" 

 return title_string

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = ""	

	return available

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract Product Price
def get_price(soup):

 try:
  price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

 except AttributeError:
  price = "" 

 return price


def scrap_amzn(link):

 header_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/103.0.5060.66 Safari/537.36",

              "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",

              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]


 user_agent = random.choice(header_list)
 header = {"User-Agent": user_agent}
 webpage = requests.get(link, headers=header, stream=True)
 # HTTP Request 
#  webpage = requests.get(link,headers=user_agent)
 
 # Soup Object containing all data
 soup = BeautifulSoup(webpage.content, "lxml")
 
 # Function calls to display all necessary product information
 print("Product Title =", get_title(soup))
 print("Product Price =", get_price(soup))
 print("Availability =", get_availability(soup))
 
 return get_title(soup),get_price(soup),get_rating(soup),get_availability(soup)



# link = input("Paste your URL ")

# scrap_amzn(link)