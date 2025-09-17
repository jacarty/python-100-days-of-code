"""
Billboard Lookup and Spotify Playlist Creation
"""

from billboard import BillboardSoup
from spotify_api import Spotify
from my_spotipy import MySpotipy
from datetime import datetime, timedelta
import sys

def main(date):
    ##############################################
    # Find previous Saturday to get Billboard Date
    ##############################################

    # Parse the input date
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get day of week (0=Monday, 5=Saturday, 6=Sunday)
    days_since_saturday = (date.weekday() + 1) % 7
    
    # If it's already Saturday, use it; otherwise go to previous Saturday
    if days_since_saturday == 0:
        billboard_date = date
    else:
        billboard_date = date - timedelta(days=days_since_saturday)
    
    billboard_date_str = billboard_date.strftime("%Y-%m-%d")

    ##############################################
    # Billboard Soup - Get Top100 for Week
    ##############################################

    # date = "2000-08-19"
    soup = BillboardSoup()
    top_100 = soup.get_chart(date=billboard_date_str)
    # print(top_100)

    ##############################################
    # Spotify - Lookup Top 100
    ##############################################

    spotify = Spotify()
    track_uris = []

    for title, artist in top_100.items():
        uri = spotify.search_track(artist_name=artist, track_name=title)
        if uri:
            track_uris.append(uri.split(":")[2])
            print(f"✓ Found: {title} - {artist}")
        else:
            print(f"✗ Not found: {title} - {artist}")
    # print(track_uris)

    ##############################################
    # Spotipy - Create Playlist for Top 100
    ##############################################

    playlist_name = f"Billboard 100 - {billboard_date_str}"
    spotipy = MySpotipy()
    spotipy.create_playlist(playlist_name, f"Playlist for the week {billboard_date_str}")
    spotipy.add_to_playlist(playlist_name, track_uris)

    ##############################################
    # Results
    ##############################################

    print(f"\n📊 Playlist Statistics:")
    print(f"   Date: {billboard_date_str}")
    print(f"   Found: {len(track_uris)}/{len(top_100)} tracks")
    print(f"   Success rate: {len(track_uris)/len(top_100)*100:.1f}%")
    print(f"   Playlist: {playlist_name}")


if __name__ == "__main__":
    default_date = "2000-08-19"
    
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        user_input = input(f"Enter date (YYYY-MM-DD) [default: {default_date}]: ")
        date_str = user_input if user_input else default_date
    
    main(date_str)
