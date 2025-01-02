from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your Next.js frontend URL like 'http://localhost:3000'
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

class SongRequest(BaseModel):
    song_name: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the SpotYT API"}

@app.post("/find-song")
def find_song(song_request: SongRequest):
    song_name = song_request.song_name
    # Logic to search for songs on Spotify and YouTube
    # Example: Send API requests to Spotify & YouTube APIs to fetch data
    
    # For simplicity, return a mock response for now
    print(song_name)
    return {"spotify": f"Spotify link for {song_name}", "youtube": f"YouTube link for {song_name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
