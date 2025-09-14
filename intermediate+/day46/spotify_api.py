from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

class Spotify:
    """This class is responsible for talking to the Spotify API."""
    
    def __init__(self):
        self.api_url = "https://api.spotify.com/v1"
        self.session = requests.Session()
        self.access_token = None
        self.token_expires = None
        
        # Load credentials once during initialization
        load_dotenv("../../.env")
        self.spotify_id = os.getenv("SPOTIFY_ID")
        self.spotify_secret = os.getenv("SPOTIFY_SECRET")
        self.spotify_userid = os.getenv("SPOTIFY_USERID")

    def login(self):
        """Login to Spotify and get Bearer - only if needed"""
        
        # Check if we already have a valid token
        if self.access_token and self.token_expires:
            if datetime.now() < self.token_expires:
                return  # Token still valid, no need to login again
        
        login_url = "https://accounts.spotify.com/api/token"
        
        login_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        login_data = {
            "grant_type": "client_credentials",
            "client_id": self.spotify_id,
            "client_secret": self.spotify_secret,
        }
        
        login = requests.post(url=login_url, headers=login_headers, data=login_data)
        
        if login.status_code == 200:
            login_result = login.json()
            self.access_token = login_result.get("access_token")
            
            # Calculate when token expires (subtract 5 minutes for safety)
            expires_in = login_result.get("expires_in", 3600)
            self.token_expires = datetime.now() + timedelta(seconds=expires_in - 300)
            
            # Update session headers with the new token
            self.session.headers.update({
                "Authorization": f"Bearer {self.access_token}"
            })
            
            return login_result
        else:
            print(f"Authentication failed: {login.status_code}")
            return None

    def search_track(self, artist_name, track_name, year=None):
        """Returns the URI of a track in Spotify for GB market."""
        
        self.login()
        
        # Build query
        if year:
            query = f"artist:{artist_name} track:{track_name} year:{year}"
        else:
            query = f"artist:{artist_name} track:{track_name}"
        
        params = {
            "q": query,
            "type": "track",
            "limit": 1,
            "market": "GB"
        }
        
        # Use session.get instead of requests.get
        # Headers are already set in the session
        search_api = f"{self.api_url}/search"
        response = self.session.get(f"{search_api}", params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data["tracks"]["items"]:
                return data["tracks"]["items"][0]["uri"]
        return None
