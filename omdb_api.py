from os import environ
import requests


api_key = environ.get("OMDB_API_KEY")  # Get env variable
title = "tt3896198"  # put imdb movie id
url = "http://www.omdbapi.com"
params = {"i": title, "apikey": api_key}

r = requests.get(url, params)
data = r.json()
print(f"Film Title: {data['Title']}")
print(f"Year: {data['Year']}")
print(f"Director: {data['Director']}")
print(f"IMDB ID: {data['imdbID']}")
print(f"Poster: {data['Poster']}")
