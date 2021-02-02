from bs4 import BeautifulSoup
import requests
import random

url = "https://www.imdb.com/chart/top"
sauce = requests.get(url)
soup = BeautifulSoup(sauce.content, 'html.parser')

tbody = soup.tbody
soup_rows =tbody.find_all('td', class_='titleColumn')


def film_scrapper():
    film_list = []
    for i in soup_rows:
        rank = i.contents[0].strip()
        title = i.a.text
        year = i.span.text
        film_list.append([rank, title, year])
    return film_list

movies = film_scrapper()
print(movies)