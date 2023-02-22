# SpotifyRipper

This Project enables you to automatically download your Spotify Tracks from a playlist of your choice in 320 kbit/s quality. Additionally the original Spotify Cover is added on top of your .mp3 track to ensure that you have the same feel like you would on Spotify.

**Version: v1.0.0**


## Installation

[Python](https://www.python.org/) version 3.x is required.

At first, install all requirements. You can also do this in a virtual environment.
```console
pip install -r requirements.txt
```

To initialize the application run this for one time:
```console
python app.py
```

Or on Linux:
```console
python3 app.py
```

## Usage

Before your can start, you have to deposit your [spotify access](https://developer.spotify.com/dashboard/applications) information.

```json
{
    "api_client" : "YOUR CLIENT",
    "api_secret" : "YOUR SECRET",
    "spotify_username" : "YOUR SPOTIFY USERNAME",
    "album_id" : "YOUR ALBUM ID"
}
```

To download an Album from your Spotify account via Youtube, you also have to entry your Username and The ID of the Album.

You can find the ID at the end of the URL when you open the playlist in the browser.

To start the download run this again:

```console
python app.py
```

