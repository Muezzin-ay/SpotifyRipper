
import urllib


class NameTools:

    @staticmethod
    def clean_name(name) :
        new_name = name\
            .replace(" ", "+")\
            .replace("ë", "e")\
            .replace("ä", "ae")\
            .replace("ü", "ue")\
            .replace("ö", "oe")\
            .replace(":", "")\
            .replace("<", "")\
            .replace(">", "")\
            .replace("/", "")
            
        new_name = urllib.parse.quote_plus(new_name)
        return new_name

    @staticmethod
    def gen_file_name(song) :
        file_name = f'{song.artist} - {song.name}'\
            .replace("/", "")\
            .replace("\\", "")\
            .replace("  ", " ")
        
        return file_name
    
    @staticmethod
    def gen_comparable_name(original_name) :
        name = original_name\
            .lower()\
            .replace(" ", "")\
            .replace("-", "")
        
        return name