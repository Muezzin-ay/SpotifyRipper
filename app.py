
import sys
import threading

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song_edit import SongEditor
from modules.config_handler import *



OUTPUT_LOCATION = './out/'


def main() :
    settings = ConfigHandler.load_settings()
    sp_api = SpotifyApi(settings['api_client'], settings['api_secret'])

    album_creator = settings['spotify_username']
    album_id = settings['album_id']
    sp_api.get_songs_from_playlist(album_creator, album_id)

    song_queue = sp_api.format_output()
    handle_playlist(song_queue)        
    

def handle_playlist(song_queue) :
    while True :
        if threading.active_count() < 25 : #number of active threads
            song = song_queue.get()

            download_thread = threading.Thread(target=download_song, args=[song])
            download_thread.start()
            threading.Thread(target=revise_song, args=[song, download_thread]).start()

        if song_queue.empty() :
            print("[MAIN] Started all Threads!")
            break


def revise_song(song, download_thread) :
    editor = SongEditor(song, OUTPUT_LOCATION)
    editor.download_cover()

    download_thread.join()

    editor.merge_cover()
    editor.add_audio_tags()


def download_song(song) :
    print("Starting Downloading!")
    yt = YoutubeApi(OUTPUT_LOCATION)
    url = yt.search_song(song)
    yt.download([url], song)



if __name__ == '__main__' :
    if not ConfigHandler.check_settings_file() :
        print("Please add your Login data!")
        sys.exit(0)
    main()