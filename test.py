from bs4 import BeautifulSoup
from lxml import etree
import requests
py_url = "https://en.wikipedia.org/wiki/Main_Page/Welcome_to_Wikipedia"
link = requests.get(py_url)
print(link.content)
py_soup = BeautifulSoup(link.content, "html.parser")
dom = etree.HTML (str(py_soup))
print (dom.xpath ('//*[@id="firstHeading"]')[0].text)


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
        await message.answer(f'Title: {title}, Price: {price}')
    
    