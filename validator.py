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

