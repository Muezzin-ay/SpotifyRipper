from modules.spotify import SpotifyApi

def main() :
    sp_api = SpotifyApi()
    sp_api.get_songs_from_playlist("OfficerAlex","0jZnctaVSmdfqtwdGGmhDO")
    song_objects_list = sp_api.format_output()




if __name__ == '__main__' :
    main()
