from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(response, "html.parser")
news_articles = []

titles = soup.select(selector=".title .titleline")

for title in titles:
    article_title = title.select_one(selector="a")
    score = title.find_next(name="span", class_="score")
    if score != None:
        score = int(score.string.split(" ")[0])
    else:
        score = 0
    news_articles.append({"title" : article_title.string, "link": article_title['href'], "score" : score})

sorted_news_articles = sorted(news_articles, key=lambda x: x['score'], reverse=True)

for i in range(5):
    print(f"Title: {sorted_news_articles[i]['title']}, Link: {sorted_news_articles[i]['link']}, Score: {sorted_news_articles[i]['score']}")