
from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
#from modules.song import Song


def main() :
    sp_api = SpotifyApi()
    sp_api.get_songs_from_playlist("OfficerAlex","0jZnctaVSmdfqtwdGGmhDO")
    song_object_list = sp_api.format_output()

    yt = YoutubeApi()
    urls = yt.search_song(song_object_list[0])
    print(urls)




if __name__ == '__main__' :
    main()
