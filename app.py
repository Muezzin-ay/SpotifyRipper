
from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
#from modules.song import Song


def main() :
    sp_api = SpotifyApi()
    sp_api.get_songs_from_playlist("OfficerAlex","0jZnctaVSmdfqtwdGGmhDO")
    song_object_list = sp_api.format_output()

    yt = YoutubeApi()
    scratched_urls = []

    for song in song_object_list[4:] :
        url = yt.search_song(song)
        scratched_urls.append(url)

    print(scratched_urls)
    yt.download(scratched_urls)




if __name__ == '__main__' :
    main()
