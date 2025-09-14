from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class MySpotipy(spotipy.Spotify):
    """This class is responsible for talking using Spotipy."""
    
    def __init__(self):        
        # Load credentials once during initialization
        load_dotenv("../../.env")

        spotify_scopes = " ".join([
            "playlist-modify-public",
            "playlist-modify-private",
            "playlist-read-private",
            "user-library-read",
            "user-library-modify",
            "user-top-read",
            "user-read-recently-played",
            "user-follow-read",
            "user-follow-modify"
        ])

        auth_manager = SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_ID"),
            client_secret=os.getenv("SPOTIFY_SECRET"),
            redirect_uri="http://127.0.0.1:3000",
            scope=spotify_scopes
        )

        super().__init__(auth_manager=auth_manager)
        self.user_id = self.me()['id']

    def create_playlist(self, playlist_name, description="", public=False):
        """Creates a playlist for a user
        
        Args:
            playlist_name: Name of the playlist
            description: Description of the playlist (optional)
            public: Whether playlist should be public (default False)
        """
        
        result = self.user_playlist_create(
            user=self.user_id, 
            name=playlist_name, 
            description=description,
            public=public
        )
        print(f"Created {'public' if public else 'private'} playlist: {playlist_name}")
        return result

    def get_playlist_id_by_name(self, playlist_name):
        """Get playlist ID from playlist name"""
        playlists = self.current_user_playlists()
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                return playlist['id']
        return None

    def add_to_playlist(self, playlist_name, uris):
        """Adds a song to an existing playlist for a user
        
        Args:
            playlist_name: Name of the playlist
            uris: a list of URI(s) that should be added to the playlist
        """
        
        playlist_id = self.get_playlist_id_by_name(playlist_name)
        if not playlist_id:
            print(f"Playlist '{playlist_name}' not found!")
            return None
        
        result = self.playlist_add_items(
            playlist_id=playlist_id,             
            items=uris,
            position=None
        )
        print(f"Added all discovered songs to playlist: {playlist_name}")
        return result
