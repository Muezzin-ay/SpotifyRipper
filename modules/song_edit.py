
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import urllib.request
import os



class SongEditor():
    def __init__(self, song, output_location) -> None:
        self.song = song
        file_name = song.get_file_name()
        self.audio_file = f"{output_location}{file_name}.mp3"
        self.picture_file = f"{output_location}{file_name}_albumcover.jpg"

    def download_cover(self):
        cover_url = self.song.cover_url
        urllib.request.urlretrieve(cover_url, self.picture_file)

    def merge_cover(self):
        audio = MP3(self.audio_file, ID3=ID3)
        try:
            audio.add_tags()
        except Exception as err:
            pass #Supressed error
            #print("[CONVERTER] Failure: Maybe no tags where added to the song!")

        picture_data = open(self.picture_file,'rb').read()
        audio.tags.add(APIC(mime='image/png', type=3, desc=u'Cover', data=picture_data))
        audio.save(self.audio_file)
        
        self.delete_cover()

    def add_audio_tags(self) :
        audio = EasyID3(self.audio_file)
        audio['artist'] = self.song.artist
        audio['title'] = self.song.name
        audio.save()

    def delete_cover(self) :
        os.remove(self.picture_file)   