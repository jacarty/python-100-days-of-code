from bs4 import BeautifulSoup
import requests

site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(site)
website_html = response.text
# print(response.text)

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

# list comprehensin for movie names; 100 to 1
movies = [movie.text for movie in soup.find_all("h3", class_="title")]

# reverse list and appeend each to file
with open("./movies.txt", "a") as f:
    for movie in reversed(movies):
        f.write(f"{movie}\n")
