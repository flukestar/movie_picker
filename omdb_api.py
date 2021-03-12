from os import environ
import requests


api_key = environ.get("OMDB_API_KEY")  # Get env variable  # put imdb movie id

url = "http://www.omdbapi.com"


def get_film_info(imdb_id):
    params = {"i": imdb_id, "apikey": api_key}
    r = requests.get(url, params)
    return r.json()
