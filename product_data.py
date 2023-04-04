# from requests_html import HTMLSession

# def Amazon(url):
#     s = HTMLSession()
#     r = s.get(url)
#     r.html.render(sleep=1)

#     title = r.html.xpath('//*[@id="productTitle"]', first=True).text
#     price = r.html.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]', first=True).text

#     print(title)
#     print(price)




# # def flipkart(url):
# #     s = HTMLSession()
# #     r = s.get(url)
# #     r.html.render(sleep=1)

# #     title = r.html.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]', first=True).text
# #     price = r.html.xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/h1/span', first=True).text
    

# #     print(title)
# #     print(price)


# website = int(input("Select the website \n1.Amazon\n2.flipkart\n"))

# if website == 1:
#     url = input("Paste your product URL: ")
#     Amazon(url)
# # if website == 2:
# #     url = input("Paste your product URL: ")
# #     flipkart(url)

import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/'
search_query = 'iphone 12'

# Send a GET request to the Flipkart search page
response = requests.get(url + 'search?q=' + search_query)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product containers on the page
product_containers = soup.find_all('div', {'class': '_2kHMtA'})

# Extract the title and price of each product
for container in product_containers:
    title = container.find('div', {'class': '_4rR01T'}).text
    price = container.find('div', {'class': '_30jeq3 _1_WHN1'}).text
    print(f'Title: {title}, Price: {price}')
