# Mood-Based Playlist Generator 🎵✨

A web app that generates **niche, mood-based playlists** and allows you to save them directly to Spotify. It dynamically changes the site background color and text to reflect your mood.  

Built with **FastAPI**, **React**, **TailwindCSS**, and **OpenAI** for AI-driven music recommendations.

---

## Features

- Generate playlists based on user mood using AI
- Focus on **fresh, niche songs** — avoid mainstream hits
- Dynamically update **background color** and text based on mood
- Save playlists to your **Spotify account**
- Responsive UI built with **TailwindCSS**
- Separate frontend (React) and backend (FastAPI)

---

## Screenshots

*Optional: Add screenshots of the app here to show UI, playlist cards, mood color changes, and Spotify integration.*

---

## Tech Stack

- **Backend:** FastAPI, Python, OpenAI API
- **Frontend:** React, TailwindCSS, Axios
- **Authentication:** Spotify OAuth2
- **State Management:** React hooks
- **Session Management:** FastAPI SessionMiddleware

---

## Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/mood-playlist.git
cd mood-playlist
```

### 2️⃣ Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
#### Create a .env file:
