import requests
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
TMDB_KEY = os.getenv("TMDB_KEY")
URL = "https://api.themoviedb.org/3/search/movie"


film = "Star Wars"

headers = {
    "Authorization": f"Bearer {TMDB_TOKEN}"
} 

params = {
    "query": film,
    "include_adult": "true"
}

response = requests.get(URL, headers=headers, params=params)
data = response.json()
movies = data['results']

# Print first 5 results
for movie in movies[:5]:
    print(f"ID: {movie['id']}")
    print(f"Title: {movie['title']}")
    print(f"Release: {movie['release_date']}")
    print(f"Rating: {movie['vote_average']}")
    print(f"Poster: https://image.tmdb.org/t/p/w500{movie['poster_path']}")
    print("-" * 50)


DETAILS = f"https://api.themoviedb.org/3/movie/{movie['id']}"

details = requests.get(DETAILS, headers=headers)
data = response.json()
print(data)