import unicodedata
import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
soup = BeautifulSoup(response, 'html.parser')

all_movies = soup.find_all('h3', class_='title')
movies_list = []

for movie in all_movies:
    content = movie.text.strip()
    title = content.split(" ", maxsplit=1)[1]
    ranking_text = content.split(' ')[0]
    ranking = int(''.join(filter(str.isdigit, ranking_text)))
    movies_list.append({
        "title": title,
        "ranking": ranking  # Assuming the year is always the last word in the title
    })
    

movies_list.sort(key=lambda x: x["ranking"])  # Sorting movies by ranking in ascending order

with open('Day 045/movies.txt', 'w') as file:
    for movie in movies_list:
        clean_title = unicodedata.normalize('NFKD', movie['title']).encode('ascii', 'ignore').decode('ascii')
        file.write(f"{movie['ranking']}) {clean_title}\n")