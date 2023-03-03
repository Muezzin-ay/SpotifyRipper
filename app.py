
import sys
import threading

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song_edit import SongEditor
from modules.config_handler import *



OUTPUT_LOCATION = './out/'


class Ripper:
    def __init__(self, argv) :
        self.argv = argv
        self.keywords = ""
        
        if not ConfigHandler.check_settings_file() :
            print("[RIPPER] Please add your Login data!")
            sys.exit(0)

        settings = ConfigHandler.load_settings()
        self.spotify_api = SpotifyApi(settings['api_client'], settings['api_secret'], settings['spotify_username']) 
        self.run()


    def run(self) :
        if self.argv[1] == "-p" :
            self.keywords = " ".join(self.argv[1:])
            self.handle_spotify_album()
        else :
            self.keywords = " ".join(self.argv[2:])
            self.handle_single_song()
            

    def handle_single_song(self) :
        self.song_queue = self.spotify_api.search_for_song(self.keywords)
        self.handle_queue()

    def handle_spotify_album(self) :
        self.song_queue = self.spotify_api.get_songs_from_playlist(self.keywords)
        self.handle_queue()


    def handle_queue(self) :
        while True :
            if threading.active_count() < 25 : #number of active threads
                song = self.song_queue.get()

                download_thread = threading.Thread(target=self.download_song, args=[song])
                download_thread.start()
                threading.Thread(target=self.revise_song, args=[song, download_thread]).start()

            if self.song_queue.empty() :
                print("[MAIN] Started all Threads!")
                break

    def download_song(self, song) :
        yt = YoutubeApi(OUTPUT_LOCATION)
        url = yt.search_song(song)
        yt.download([url], song)

    def revise_song(self, song, download_thread) :
        editor = SongEditor(song, OUTPUT_LOCATION)
        editor.download_cover()

        download_thread.join()

        editor.merge_cover()
        editor.add_audio_tags()




if __name__ == '__main__' :
    app = Ripper(sys.argv)