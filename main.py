from bs4 import BeautifulSoup
import requests
import random

url = "https://www.imdb.com/chart/top"
sauce = requests.get(url)
soup = BeautifulSoup(sauce.content, "html.parser")
tbody = soup.tbody
soup_rows = tbody.find_all("tr")


def film_scrapper():
    film_list = []
    for i in soup_rows:
        tcol = i.find("td", class_="titleColumn")
        rank = tcol.contents[0].strip()
        title = tcol.a.text
        year = tcol.span.text
        poster = i.img["src"]
        film_list.append([rank, title, year, poster])
    return film_list


def pick_movie():
    movie = film_scrapper()
    return random.choice(movie)


if __name__ == "__main__":
    pick_movie()
