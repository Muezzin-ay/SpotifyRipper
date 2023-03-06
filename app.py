
from queue import Queue
from threading import Thread, active_count
import sys

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.song_edit import SongEditor
from modules.config_handler import ConfigHandler



OUTPUT_LOCATION = './out/'
NUMBER_OF_THREADS = 25


class Ripper:
    def __init__(self, argv) :
        self.argv = argv
        self.song_queue = Queue()
        
        if not ConfigHandler.check_settings_file() :
            print("[MAIN] Please add your Login data!")
            sys.exit(0)

        settings = ConfigHandler.load_settings()
        self.spotify_api = SpotifyApi(settings['api_client'], settings['api_secret'], settings['spotify_username']) 
        self.run()

    def run(self) :
        if self.argv[1] == "-p" :
            playlist_id = self.argv[2]
            self.spotify_api.get_songs_from_playlist(playlist_id, self.song_queue)
        else :
            search_words = " ".join(self.argv[1:])
            self.spotify_api.search_for_song(search_words, self.song_queue)
        self.handle_queue()


    def handle_queue(self) :
        print("[MAIN] Started handling...")
        while True :
            if active_count() < NUMBER_OF_THREADS : #number of allowed active threads
                song = self.song_queue.get()

                download_thread = Thread(target=self.download_song, args=[song])
                download_thread.start()
                Thread(target=self.revise_song, args=[song, download_thread]).start()

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