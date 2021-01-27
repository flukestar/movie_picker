from bs4 import BeautifulSoup
import requests
import random

url = "https://www.imdb.com/chart/top"
sauce = requests.get(url)
soup = BeautifulSoup(sauce.content, 'html.parser')

soup_trows = soup.find_all('td', class_ = 'titleColumn')

def movie_picker():
    movie_list = []
    for i in (soup_trows):
        movie_list.append(i.a.text)

    picker = random.choice(movie_list)
    print(picker)

movie_picker()