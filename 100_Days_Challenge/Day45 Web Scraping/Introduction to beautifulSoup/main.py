import bs4

HTMLPOS = "./website.html"

with open(HTMLPOS) as webpage:
    contents = webpage.read()
    
soup = bs4.BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
# print(soup.prettify())

print(soup.find_all(name="a"))

for tag in  soup.find_all(name="a"):
    print(tag.getText())
    print(tag.get("href"))
    
print(soup.find_all(name="h3", class_="heading"))

company_url = soup.select_one(selector="p a")
print(company_url)

company_url = soup.select_one(selector=".heading")
print(company_url)