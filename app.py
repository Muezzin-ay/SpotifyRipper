
import sys

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.pullcover import SpotifyCoverLoader
from modules.name_tools import NameTools
from modules.config_handler import *


def main() :
    settings = ConfigHandler.load_settings()
    sp_api = SpotifyApi(settings['api_client'], settings['api_secret'])

    album_creator = settings['spotify_username']
    album_id = settings['album_id']
    sp_api.get_songs_from_playlist(album_creator, album_id)

    song_object_list = sp_api.format_output()

    yt = YoutubeApi()

    for song in song_object_list : #[:3]
        url = yt.search_song(song)
        print(song)
        file_name = NameTools.gen_file_name(song.name, song.artist)

        yt.download([url], file_name)

        scl = SpotifyCoverLoader(song.album_url)
        scl.download_cover()
        scl.merge_cover(file_name,song.artist)


if __name__ == '__main__' :
    if not ConfigHandler.check_settings_file() :
        print("Please add your Login data!")
        sys.exit(0)
    main()
