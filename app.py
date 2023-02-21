
import sys
import threading
import queue

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song_edit import SongEditor
from modules.name_tools import NameTools
from modules.config_handler import *


def main() :
    settings = ConfigHandler.load_settings()
    sp_api = SpotifyApi(settings['api_client'], settings['api_secret'])

    album_creator = settings['spotify_username']
    album_id = settings['album_id']
    sp_api.get_songs_from_playlist(album_creator, album_id)

    song_object_list = sp_api.format_output()
    handle_playlist(song_object_list)        


def handle_playlist(song_object_list) :
    song_queue = queue.Queue()
    [song_queue.put(song) for song in song_object_list]

    while True :
        if threading.active_count() < 10 : #10 active threads
            song = song_queue.get()
            t = threading.Thread(target=download_song, args=[song])
            t.start()

        if song_queue.empty() :
            print("[MAIN] Started all Threads!")
            break


def download_song(song) :
    file_name = NameTools.gen_file_name(song)

    yt = YoutubeApi()
    url = yt.search_song(song)
    yt.download([url], file_name)

    editor = SongEditor(song.album_url)
    editor.download_cover(file_name)
    editor.merge_cover(file_name, song.artist)



if __name__ == '__main__' :
    if not ConfigHandler.check_settings_file() :
        print("Please add your Login data!")
        sys.exit(0)
    main()