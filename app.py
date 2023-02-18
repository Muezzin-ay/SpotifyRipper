
from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song import Song


def main() :
    #sp_api = SpotifyApi()
    #sp_api.log_into_spotify_api()

    yt = YoutubeApi()

    song = Song("come2gether", "ooyy", 5000)
    url = yt.search_song(song)[0]
    yt.download(url)




if __name__ == '__main__' :
    main()
