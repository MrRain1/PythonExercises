# Webpages are plain text files formatted in html 
# It can be parsed with the Beautiful soup module

# we pass the string with the hrml to the .BeautifulSoup() function 
# to get a Soup object

# the Soup obj ha s a select() method that can be passed a string of 
# the CSS selector for an HTML tag

# the select() method will return a list of matching Elements objects

import bs4, requests

def getAmznPrice (productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("<Insert CSS>")
    return elems[0].text.strip()

price = getAmznPrice("<Insert URL>")
print(f"The price is: {price}")