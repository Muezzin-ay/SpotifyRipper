

class Song():
    def __init__(self, name, artist, duration) :
        self.name = name
        self.artist = artist
        self.duration = duration

    def get_search_word(self) :
        searchable_name = self.name.replace(" ", "+")
        searchable_artist = self.artist.replace(" ", "+")
        search_name = f'{searchable_name}+{searchable_artist}'
        return search_name
    
    def __repr__(self) -> str:
        return self.get_search_word()
        