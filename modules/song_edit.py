
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import urllib.request
import os

from modules.web_scratch import WebScratch


class SongEditor():
    def __init__(self, song, output_location) -> None:
        self.song = song
        file_name = song.get_file_name()
        self.audio_file = f"{output_location}{file_name}.mp3"
        self.picture_file = f"{output_location}{file_name}_albumcover.jpg"

        self.load_thumbnail_url()

    def load_thumbnail_url(self) :
        html = urllib.request.urlopen(self.song.album_url).read()
        #do not know why, but it works; finds thumbnail url using regex
        html_source = html.decode('utf-8').encode('cp850','replace').decode('cp850')
        self.thumbnail_url = WebScratch.extract_thumbnail_url(html_source)

    def download_cover(self):
        urllib.request.urlretrieve(self.thumbnail_url, self.picture_file)

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