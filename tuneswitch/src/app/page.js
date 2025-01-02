"use client"

import { useState } from "react";
import axios from "axios";

export default function Home() {
    const [song, setSong] = useState("");
    const [results, setResults] = useState(null);

    const searchSong = async () => {
        try {
          const response = await axios.post("http://localhost:8000/find-song", { song_name: song });
          setResults(response.data);
        } catch (error) {
          console.error(error);
        }
    };

    return (
        <div className="flex flex-col gap-4 items-center justify-center mt-12">
        <input
            type="text"
            value={song}
            onChange={(e) => setSong(e.target.value)}
            placeholder="Enter song name"
            className="input text-black outline-none"
        />
        <button onClick={searchSong} className="bg-white text-black p-2">Search</button>

        {results && (
            <div>
            <h3>Results:</h3>
            <p>Spotify: {results.spotify}</p>
            <p>YouTube: {results.youtube}</p>
            </div>
        )}
        </div>
    );
}
