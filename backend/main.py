from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os, json, urllib.parse
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from spotify_utils import get_auth_url, get_access_token, create_spotify_playlist
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

class MoodRequest(BaseModel):
    text: str

class Song(BaseModel):
    title: str
    artist: str

class PlaylistResponse(BaseModel):
    playlist: List[Song]
    mood_color: str

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

app = FastAPI()

# allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000", 
        "https://mood-tune.vercel.app/", 
        "https://moodtune-l8t8.onrender.com"
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.add_middleware(
    SessionMiddleware,
    secret_key = os.getenv("SESSION_SECRET_KEY", "supersecretkey"),
    same_site = "lax"
)

@app.post("/playlist", response_model=PlaylistResponse)

async def generate_playlist(request: MoodRequest):
    user_text = request.text

    # --- 1️⃣ Generate niche playlist ---
    playlist_prompt = f"""
    The user is feeling: '{user_text}'.
    Suggest a random number of **niche, fresh songs** that match this mood. Make sure the number 
    of songs in the playlist is greater than **ten**
    Avoid mainstream hits; focus on music the user is unlikely to have heard before.
    Return ONLY a JSON array of objects like:
    [
      {{"title": "Song1", "artist": "Artist1"}},
      {{"title": "Song2", "artist": "Artist2"}},
      {{"title": "Song3", "artist": "Artist3"}},
      {{"title": "Song4", "artist": "Artist4"}},
      {{"title": "Song5", "artist": "Artist5"}},
      {{"title": "Song6", "artist": "Artist6"}},
      {{"title": "Song7", "artist": "Artist7"}},
      {{"title": "Song8", "artist": "Artist8"}},
      {{"title": "Song9", "artist": "Artist9"}},
      {{"title": "Song10", "artist": "Artist10"}}
    ]
    """

    try:
        playlist_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": playlist_prompt}],
            temperature=0.8
        )

        # Extract content safely
        choice = playlist_response.choices[0]
        if hasattr(choice.message, "content"):
            playlist_content = choice.message.content.strip()
        else:
            playlist_content = choice.message["content"].strip()

        # Remove ```json fences
        if playlist_content.startswith("```json"):
            playlist_content = playlist_content[len("```json"):].strip()
        if playlist_content.endswith("```"):
            playlist_content = playlist_content[:-3].strip()

        try:
            playlist = json.loads(playlist_content)
        except Exception as e:
            print(f"Playlist JSON parsing error: {e}")
            playlist = [
                {"title": "Fallback Song 1", "artist": "Fallback Artist 1"},
                {"title": "Fallback Song 2", "artist": "Fallback Artist 2"},
                {"title": "Fallback Song 3", "artist": "Fallback Artist 3"},
                {"title": "Fallback Song 4", "artist": "Fallback Artist 4"},
                {"title": "Fallback Song 5", "artist": "Fallback Artist 5"},
                {"title": "Fallback Song 6", "artist": "Fallback Artist 6"},
                {"title": "Fallback Song 7", "artist": "Fallback Artist 7"},
                {"title": "Fallback Song 8", "artist": "Fallback Artist 8"},
                {"title": "Fallback Song 9", "artist": "Fallback Artist 9"},
                {"title": "Fallback Song 10", "artist": "Fallback Artist 10"}
            ]

        # --- 2️⃣ Generate mood color ---
        color_prompt = f"""
        The user is feeling: '{user_text}'.
        Return a single JSON object with a HEX color that best represents this mood.
        Example: {{"mood_color": "#A1B2C3"}}
        Return only valid JSON, no extra text.
        """
        color_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": color_prompt}],
            temperature=0.5
        )

        # Extract color content safely
        color_choice = color_response.choices[0]
        if hasattr(color_choice.message, "content"):
            color_content = color_choice.message.content.strip()
        else:
            color_content = color_choice.message["content"].strip()

        # Remove ```json fences
        color_content = color_content.replace("```json", "").replace("```", "").strip()
        print(color_content)

        try:
            color_data = json.loads(color_content)
            mood_color = color_data.get("mood_color", "#E5E7EB")
        except Exception as e:
            # Fallback: extract HEX code manually
            import re
            match = re.search(r"#([A-Fa-f0-9]{6})", color_content)
            if match:
                mood_color = f"#{match.group(1)}"
            else:
                print(f"Color JSON parsing error: {e}")
                mood_color = "#E5E7EB"

        # --- 3️⃣ Combine and return ---
        print("Sending Response:" , {"playlist": playlist, "mood_color": mood_color})
        return {
            "playlist": playlist,
            "mood_color": mood_color
        }

    except Exception as e:
        print("OpenAI API call failed:", e)
        return {
            "mood_color": "#E5E7EB",
            "playlist": [
                {"title": "Fallback Song 1", "artist": "Fallback Artist 1"},
                {"title": "Fallback Song 2", "artist": "Fallback Artist 2"},
                {"title": "Fallback Song 3", "artist": "Fallback Artist 3"},
                {"title": "Fallback Song 4", "artist": "Fallback Artist 4"},
                {"title": "Fallback Song 5", "artist": "Fallback Artist 5"}
            ]
        }

@app.get("/login")
def login_spotify(mood: str, songs: str):
    encoded_data = urllib.parse.quote(json.dumps({"songs": json.loads(songs), "mood": mood}))
    return RedirectResponse(url=f"{get_auth_url()}&state={encoded_data}")

@app.get("/callback")
def spotify_callback(state: str, code: str):
    print("Recieved code: ", code)

    #Excange code for access token
    token_info = get_access_token(code)
    access_token = token_info.get("access_token")
    playlist_data = json.loads(urllib.parse.unquote(state))
    if playlist_data and access_token:
        songs = playlist_data["songs"]
        mood = playlist_data["mood"]

        playlist_url = create_spotify_playlist(access_token, songs, mood)
        print("🎵 Created playlist: ", playlist_url)

        return RedirectResponse(playlist_url)

    return {"error" : "No playlist in session or failed access token", "token_info": token_info}

@app.post("/spotify_playlist")
def make_spotify_playlist(data: dict):
    access_token = data["access_token"]
    songs = data["songs"]
    mood = data.get("mood", "mood")

    playlist_url = create_spotify_playlist(access_token, songs, mood)
    return {"playlist_url": playlist_url}

@app.post("/save_to_spotify")
def save_to_spotify(request: Request, data: dict):
    """Recieves AI playlist & mood and stores it in session"""
    state_data = {"songs": data["songs"], "mood": data.get("mood", "Mood Playlist")}
    encoded_state = urllib.parse.quote(json.dumps(state_data))
    login_url = get_auth_url(state=encoded_state)
    return {"login_url": login_url}
