from bs4 import BeautifulSoup
import requests

class BillboardSoup:
    #This class is responsible for talking to the Spotify API.
    
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
            }
        self.base_url = "https://www.billboard.com/charts/hot-100"

    def get_chart(self, date="2000-08-12"):
        """Get the Chart Billboard chart for the week"""

        date = date
        url = f"{self.base_url}/{date}/"

        response = requests.get(url, headers=self.header)
        website_html = response.text
        # print(response.text)

        soup = BeautifulSoup(website_html, 'html.parser')
        # print(soup.prettify())

        song_items = soup.find_all("li", class_="o-chart-results-list__item")

        titles = [item.select_one("h3", id="title-of-a-story").get_text(strip=True)
                for item in song_items 
                if item.select_one("h3", id="title-of-a-story")]

        artists = [item.select_one("span.a-no-trucate.a-font-secondary").get_text(strip=True).replace("Featuring", " Featuring ")
                for item in song_items 
                if item.select_one("span.a-no-trucate.a-font-secondary")]

        title_artist = dict(zip(titles, artists))
        return title_artist

        #print(titles)
        #print(artists)
        #print(title_artist)
