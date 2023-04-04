from bs4 import BeautifulSoup
import requests

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


# if __name__ == '__main__':

def scrap(link):
# Headers for request
 HEADERS = ({'User-Agent':
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
             'Accept-Language': 'en-US, en;q=0.5'})
 
 # The webpage URL
 URL = "https://www.amazon.in/dp/B0B3XPG9WG/ref=sspa_dk_detail_4?pd_rd_i=B0B3XPG9WG&pd_rd_w=yNNGO&content-id=amzn1.sym.b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_p=b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_r=9VHWWF1VBXKYH27PJXG5&pd_rd_wg=sv0D8&pd_rd_r=e06c1528-6474-41d0-8d6d-ebd58731e417&s=computers&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1"
 
 # HTTP Request
 webpage = requests.get(link, headers=HEADERS)
 
 # Soup Object containing all data
 soup = BeautifulSoup(webpage.content, "lxml")
 
 # Function calls to display all necessary product information
 print("Product Title =", get_title(soup))
 print("Product Price =", get_price(soup))

 return get_title(soup),get_price(soup),get_rating(soup)


