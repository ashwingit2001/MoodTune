<!-- ...existing code... -->
# MoodTune — Mood-Based Playlist Generator 🎵✨

A web app that generates niche, mood-based playlists and lets you save them to Spotify. The UI updates background color and text to reflect the chosen mood. Built with FastAPI, React, TailwindCSS, and OpenAI for AI-driven recommendations.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Notes](#notes)

---

## Features

- Generate playlists from a textual mood input using AI
- Emphasize fresh, niche tracks (avoid mainstream hits)
- Dynamic background color and text based on mood
- Save generated playlists to your Spotify account via OAuth2
- Responsive UI with TailwindCSS

---

## Tech Stack

- Backend: FastAPI, Python, OpenAI API
- Frontend: React, TailwindCSS, Axios
- Authentication: Spotify OAuth2
- Session management: FastAPI SessionMiddleware
- State: React hooks

---

## Screenshots

Add screenshots to illustrate:
- Mood input and generated playlist
- Background color / text change per mood
- Spotify save flow and "Open in Spotify" link

---

## Getting Started

### Prerequisites

- Python 3.10+ (or project-supported version)
- Node.js 16+ and npm
- A Spotify Developer app (client ID/secret) with redirect URI set
- OpenAI API key

### Backend Setup

```bash
cd backend
python -m venv venv
# Activate virtualenv:
# On macOS / Linux:
source venv/bin/activate
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On Windows (cmd.exe):
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the backend folder with the following variables:

```env
OPEN_AI_KEY=your_openai_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8000/callback
SESSION_SECRET_KEY=supersecretkey
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend will run on: http://127.0.0.1:8000

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will run on: http://localhost:3000

---

## Usage

1. Open the frontend in your browser.
2. Enter your current mood in the input box and click "Generate".
3. Review the generated niche playlist (background and text update).
4. Click "Save to Spotify" to log in and create the playlist in your Spotify account.
5. Directly Play from Spotify.

---

## Folder Structure

mood-playlist/
├─ backend/
│  ├─ main.py
│  ├─ spotify_utils.py
│  ├─ requirements.txt
│  └─ .env
├─ frontend/
│  ├─ src/
│  ├─ package.json
│  └─ tailwind.config.js
├─ README.md

---

## Notes

- Ensure the redirect URI in your Spotify Developer Dashboard matches SPOTIFY_REDIRECT_URI.
- The app purposefully prioritizes lesser-known tracks; some results may be unfamiliar.
- For local testing, run frontend on localhost:3000 and backend on localhost:8000.

<!-- ...existing code... -->