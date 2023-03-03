
from modules.name_tools import NameTools


class Song():
    def __init__(self, song_data) :
        self.name = song_data['name']
        self.artist = song_data['artists'][0]['name']
        self.duration = int(song_data['duration_ms'] / 1000)
        self.cover_url = song_data['album']['images'][0]['url']
        self.file_name = NameTools.gen_file_name(self)

    def get_search_word(self) :
        searchable_name = NameTools.clean_name(self.name)
        searchable_artist = NameTools.clean_name(self.artist)
        search_name = f'{searchable_name}+{searchable_artist}'
        return search_name
    
    def get_file_name(self) :
        return self.file_name
    
    def __repr__(self) -> str:
        return f"{self.name} from {self.artist} ({self.duration}s)"
    
    def check_duration(self, yt_duration) :
        #offset = abs(self.duration / yt_duration) #0.95 -> with Percentage
        offset = abs(self.duration - yt_duration) # with Seconds
        if offset < 3 : #3 seconds difference
            return True
        return False