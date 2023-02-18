
import json
import os

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.pullcover import SpotifyCoverLoader

def check_settings_file() :
    if not os.path.isfile('./config.json') :
        with open('./config.json', 'w') as file:
            file.write('{"api_client" : "", "api_secret" : "", "spotify_username" : ""}')
            return False
    return True

def load_settings() :
    with open('./config.json') as file:
        settings = json.load(file)
        file.close()
    return settings


def main() :
    settings = load_settings()
    sp_api = SpotifyApi(settings['api_client'], settings['api_secret'])

    album_creator = settings['spotify_username']
    album_id = "0jZnctaVSmdfqtwdGGmhDO"
    sp_api.get_songs_from_playlist(album_creator, album_id)

    song_object_list = sp_api.format_output()

    yt = YoutubeApi()

    for song in song_object_list : #[:3]
        url = yt.search_song(song)
        print(song)
        file_name = f"{song.artist} - {song.name}"

        yt.download([url], file_name)

        scl = SpotifyCoverLoader(song.album_url)
        scl.download_cover()
        scl.merge_cover(file_name,song.artist)


if __name__ == '__main__' :
    if not check_settings_file() :
        print("Please add your Login data!")
        exit()
    main()
