
from modules.name_tools import NameTools


class Song():
    def __init__(self, song_data) :
        self.name = song_data['name']
        self.duration = int(song_data['duration_ms'] / 1000)
        self.cover_url = song_data['album']['images'][0]['url']
        self.gen_artist_listing(song_data['artists'])

        self.file_name = NameTools.gen_file_name(self)

    def __repr__(self) -> str:
        return f"{self.name} from {self.artist} ({self.duration}s)"
    
    def gen_artist_listing(self, artist_data) :
        self.artist = artist_data[0]['name']
        for artist in artist_data[1:] :
            self.artist += f", {artist['name']}"

    def get_search_word(self) :
        searchable_name = NameTools.clean_name(self.name)
        searchable_artist = NameTools.clean_name(self.artist)
        search_name = f'{searchable_name}+{searchable_artist}'
        return search_name
    
    def get_file_name(self) :
        return self.file_name
    
    def check_duration(self, yt_duration) :
        #offset = abs(self.duration / yt_duration) #0.95 -> with Percentage
        offset = abs(self.duration - yt_duration) # with Seconds
        if offset < 3 : #3 seconds difference
            return True
        return False