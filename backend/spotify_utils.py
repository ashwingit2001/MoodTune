import os
import requests
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_URL = "https://api.spotify.com/v1"

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

SCOPES = "playlist-modify-public playlist-modify-private user-read-private"

def get_auth_url(state: str = None):
    """Return Spotify Login Redirect URL"""
    url = f"{SPOTIFY_AUTH_URL}?response_type=code&client_id={CLIENT_ID}&scope={SCOPES}&redirect_uri={REDIRECT_URI}"
    if(state):
        url += f"&state={urllib.parse.quote(state)}"
    return url

def get_access_token(code: str):
    """Exchange access code for auth token"""

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(SPOTIFY_TOKEN_URL, data= payload)
    return response.json()

def create_spotify_playlist(access_token: str, songs: list, mood: str = "Mood Playlist"):
    """Create playlist with returned tracks"""

    user_response = requests.get(
        f"{SPOTIFY_API_URL}/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_id = user_response.json().get("id")

    playlist_data = {
        "name": f"{mood.title()} Playlist 🎧",
        "description": f"AI-generated playlist for the mood: {mood}",
        "public": False
    }

    playlist_response = requests.post(
        f"{SPOTIFY_API_URL}/users/{user_id}/playlists",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json=playlist_data
    )

    playlist_id = playlist_response.json().get("id")

    uris = []
    for song in songs:
        query = f"{song['title']} {song['artist']}"
        search_response = requests.get(
            f"{SPOTIFY_API_URL}/search?q={query}&type=track&limit=1",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        tracks = search_response.json().get("tracks", {}).get("items", [])
        if tracks:
            uris.append(tracks[0]["uri"])

    if uris:
        requests.post(
            f"{SPOTIFY_API_URL}/playlists/{playlist_id}/tracks",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            },
            json={"uris": uris}
        )
    return f"https://open.spotify.com/playlist/{playlist_id}"
