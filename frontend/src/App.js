import React, { useEffect, useState } from "react"
import axios from "axios"

function getTextColor(bgColor) {
    if(!bgColor.startsWith("#")) return '#000000'
    const r = parseInt(bgColor.slice(1, 3), 16)
    const g = parseInt(bgColor.slice(3, 5), 16)
    const b = parseInt(bgColor.slice(5, 7), 16)
    const brightness = (r * 299 + g * 587 + b * 114) / 1000
    return brightness > 155 ? "#000000" : "#FFFFFF"
}

function App() {
    const [mood, setMood] = useState("")
    const [playlist, setPlaylist] = useState([])
    const [loading, setLoading] = useState(false)
    const [moodColor, setMoodColor] = useState("#E5E7EB")
    const [accessToken, setAccessToken] = useState("")
    const [spotifyLink, setSpotifyLink] = useState("")

    useEffect(() => {
        const params = new URLSearchParams(window.location.search)
        const token = params.get("access_token")
        if(token) setAccessToken(token)
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        if(!mood) return

        setLoading(true)
        setSpotifyLink("") // reset
        try {
            const response = await axios.post("https://moodtune-l8t8.onrender.com/playlist", {
                text: mood
        })

        console.log(response.data)
        const generatedPlaylist = response.data.playlist
        setPlaylist(generatedPlaylist)
        setMoodColor(response.data.mood_color || "#E5E7EB")
        console.log(moodColor)

        } catch (error) {
            console.error("API error: ", error)
            alert("Something went wrong. Check backend.")
        } finally {
            setLoading(false)
        }
    }

    const handleSaveSpotify = async () => {
        try {
            const response = await axios.post("https://moodtune-l8t8.onrender.com/save_to_spotify", {
                songs: playlist,
                mood
            }, {withCredentials: true})
            window.location.href = response.data.login_url; // redirect to Spotify login
        } catch (err) {
            console.error(err)
            alert("Failed to initiate Spotify save.")
        }
    }

    const textColor = getTextColor(moodColor)

    return (
    <div
      className={`min-h-screen flex flex-col items-center transition-all duration-700 ${
        playlist.length > 0 ? "pt-8 items-start" : "justify-center"
      }`}
      style={{ backgroundColor: moodColor }}
    >
      {/* Heading */}
      <div className={`text-center ${playlist.length > 0 ? "ml-8" : ""} mb-8 transition-all duration-700`}>
        <h1
          className="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-4"
          style={{ color: "#2C2C2C", textShadow: "1px 1px 4px rgba(0,0,0,0.2)" }}
        >
          Mood Tune 🎵
        </h1>
        <p className="text-lg sm:text-xl text-gray-600/90">
          Discover niche playlists that match your vibe and brighten your day.
        </p>
    </div>

      {/* Mood Input Form */}
      <form onSubmit={handleSubmit} className="flex w-full max-w-md mb-6">
        <input
          type="text"
          placeholder="How are you feeling?"
          value={mood}
          onChange={(e) => setMood(e.target.value)}
          className="flex-1 p-3 rounded-l-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-400"
        />
        <button
          type="submit"
          className="bg-green-500 text-white px-6 rounded-r-lg hover:bg-green-600 transition-colors"
        >
          Generate
        </button>
      </form>

      {/* Loading */}
      {loading && <p className="text-gray-700 mb-4 animate-pulse">Loading playlist...</p>}

      {/* Playlist Cards */}
      {playlist.length > 0 && (
        <div className="w-full flex justify-center mt-6">
          {/* <h2 className="text-xl flex font-semibold mb-4 text-gray-800" style={{ color: textColor }}>
            Playlist for "{mood}"
          </h2> */}
          <ul className="space-y-3">
            {playlist.map((song, index) => (
              <li
                key={index}
                className="bg-white/30 rounded-xl p-4 shadow-md backdrop-blur-sm text-center transform hover:scale-105 transition-transform duration-200"
              >
                <h3 className="text-lg font-semibold">{song.title}</h3>
                <p className="text-sm opacity-80">{song.artist}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Spotify Button */}
      {playlist.length > 0 && !spotifyLink && (
        <button
          onClick={handleSaveSpotify}
          className="mt-6 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition-colors"
        >
          Save to Spotify
        </button>
      )}

      {/* Spotify Playlist Link */}
      {spotifyLink && (
        <a
          href={spotifyLink}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-4 text-blue-700 font-semibold hover:underline"
        >
          Open Playlist on Spotify
        </a>
      )}
    </div>
  )
}

export default App