
from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song import Song


def main() :
    sp_api = SpotifyApi()
    sp_api.get_songs_from_playlist("OfficerAlex","0Fm8D19xbDnZlVXro7UzLC")
    song_object_list = sp_api.format_output()

    print(song_object_list)




if __name__ == '__main__' :
    main()
