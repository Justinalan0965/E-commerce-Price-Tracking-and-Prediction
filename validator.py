#Redmi Note 11 (Space Black, 4GB RAM, 64GB Storage)|90Hz FHD+ AMOLED Display | Qualcomm® Snapdragon™ 680-6nm | 33W Charger Included https://amzn.eu/d/2F3Tpuu
#Take a look at this acer Extensa Core i5 11th Gen - (8 GB/512 GB SSD/Windows 11 Home) EX 215-54-583M Thin and Light Laptop on Flipkart https://dl.flipkart.com/dl/acer-extensa-core-i5-11th-gen-8-gb-512-gb-ssd-windows-11-home-ex-215-54-583m-thin-light-laptop/p/itm03b6367174a8f?pid=COMGGYEBSGX9SEBG&cmpid=product.share.pp&_refId=PP.e931a767-0ab0-4eda-b0d2-9a53e97123dc.COMGGYEBSGX9SEBG&_appId=CL
import re

def validateamazonURL(url):
    text = url
    
    regex = r'\b(https?:\/\/)?(www\.)?(amazon|amzn)\.(com|ca|co\.uk|de|fr|in|it|co\.jp|com\.au|com\.br|com\.mx|nl|es|eu)\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)\b'

    matches = re.findall(regex, text)
    
    try:
        for match in matches:
            val = match[0] + match[1] + match[2] + "." + match[3] + match[4]

        matchFound = val is not None

        return val,matchFound
    
    except UnboundLocalError:
        val = 0
        return val,False
    
    
def validateflipURL(url):
    
    
    text = url

    pattern = r'https?://(?:www\.|dl\.)?flipkart\.com/\S+'

    matches = re.findall(pattern, text)

    try:
        val = matches[0]
        matchFound = val is not None
        return val,matchFound
        
    except (IndexError,UnboundLocalError):
        val = 0
        return val,False


# url = input("Send the URL: ")

# value,match = validateflipURL(url)

# print(value)
# print("\n")
# print(match)
