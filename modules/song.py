
from modules.str_tools import clean_name


class Song():
    def __init__(self, artist, name, duration,album_url) :
        self.name = name
        self.artist = artist
        self.duration = duration
        self.album_url = album_url

    def get_search_word(self) :
        searchable_name = clean_name(self.name)
        searchable_artist = clean_name(self.artist)
        search_name = f'{searchable_name}+{searchable_artist}'
        return search_name
    
    def __repr__(self) -> str:
        return self.get_search_word()
    
    def check_duration(self, yt_duration) :
        #offset = abs(self.duration / yt_duration) #0.95 -> with Percentage
        offset = abs(self.duration - yt_duration) # with Seconds
        if offset < 5 : #5 seconds difference
            return True
        return False