
import sys

from modules.spotify import SpotifyApi
from modules.yt_api import YoutubeApi
from modules.pullcover import SpotifyCoverLoader
from modules.str_tools import gen_file_name

from modules.multiprocess import MultiprocessStart

from modules.config_handler import *

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

def pull_spotify_info():
    settings = load_settings()
    sp_api = SpotifyApi(settings['api_client'], settings['api_secret'])

    album_creator = settings['spotify_username']
    album_id = settings['album_id']
    sp_api.get_songs_from_playlist(album_creator, album_id)

    song_object_list = sp_api.format_output()

    return song_object_list

def download_songs(song,thread_number):
    

    """
    for song in song_object_list : #[:3]
        url = yt.search_song(song)
        print(song)
        file_name = gen_file_name(song.name, song.artist)
    """
    file_name = gen_file_name(song.name, song.artist)
    yt = YoutubeApi()
    url = yt.search_song(song)
    yt.download([url], file_name)

    scl = SpotifyCoverLoader(song.album_url)
    # needs to pass song.name to add to albumcover.jpg so the system does not have problems bc several files are calles albumcover.jpg
    scl.download_cover(song.name)
    scl.merge_cover(file_name,song.artist)

def test(a):

    print("test")

def main() :
    # Pulls info from spotify using the spotify api
    song_object_list = pull_spotify_info()

    # Searches Youtube to find the matching song, downloads it and adds the specific cover
    mp = MultiprocessStart()
    mp.start_threaded_download(amount_of_threads=6 ,target_function=download_songs,song_object_list=song_object_list)
    #mp.start_multiple_instances(amount_of_threads=6,)
    #download_songs(song_object_list)




if __name__ == '__main__' :
    if not ConfigHandler.check_settings_file() :
        print("Please add your Login data!")
        sys.exit(0)
    main()