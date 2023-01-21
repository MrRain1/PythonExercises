import requests
from bs4 import BeautifulSoup

resp = requests.get("https://news.ycombinator.com/news")

yc_webpage = resp.text
soup= BeautifulSoup(yc_webpage, "html.parser")

news= soup.select(selector=".titlelink")
news_text = [article.getText() for article in news]
news_link = [article.get("href") for article in news]
news_upvotes = [int(points.getText().split(" ")[0]) for points in soup.select(selector=".score")]
articles =[]

print(news_upvotes)

if len(news_text) == len(news_link) and len(news_text) == len(news_upvotes):
    for index in range(len(news_text)):
        articles.append((news_text[index], news_link[index], news_upvotes[index]))
        
for index in range(len(articles)):
    print(articles[index])