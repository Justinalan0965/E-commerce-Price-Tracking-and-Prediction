import bs4
import urllib.request

#.replace(",","").replace("₹","")

def flipkart_details(url):

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    name = soup.find('span',class_="B_NuCI").text
    price = soup.find('div',class_="_30jeq3 _16Jk6d").text
    # availabile = soup.find('div',class_="_1dVbu9").string
    ratings = soup.find('div',class_="_2d4LTz").text + " out of 5"

    print(name,price,ratings)


def amazon_details(url):

    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    title = soup.find("span", attrs={"id":'productTitle'})
    title_value = title.string
    name = title_value.strip()

    available = soup.find("div", attrs={'id':'availability'})
    available = available.find("span").string.strip()

    rating = rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()

    price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
		
    return name,price,rating,available



# url = input("Enter your URl: ")

# flipkart_details(url)



