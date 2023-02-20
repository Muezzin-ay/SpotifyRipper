
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import urllib.request
import re
import os

from modules.str_tools import clean_name


class SpotifyCoverLoader():
    def __init__(self, album_url) -> None:
        pattern = r'loading="eager" src="([^ ]*)"'

        #do not know why, but it works; finds thumbnail url using regex
        html = urllib.request.urlopen(album_url).read()
        html_source = html.decode('utf-8').encode('cp850','replace').decode('cp850')
        thumbnail_url = re.findall(pattern, html_source)

        print(thumbnail_url)
        self.thumbnail_url = thumbnail_url[0]

    def download_cover(self):
        print(self.thumbnail_url)
        urllib.request.urlretrieve(self.thumbnail_url, "./out/albumcover.jpg")

    def merge_cover(self, file_name, artist):
        clean_file_name = file_name.replace(':','#')
        if not '(' in clean_file_name and not ')' in clean_file_name :
            clean_file_name = clean_name(file_name)

        audio_file = f"./out/{clean_file_name}.mp3"
        picture_file = "./out/albumcover.jpg"

        audio = MP3(audio_file, ID3=ID3)
        try:
            audio.add_tags()
        except Exception as err:
            print("Error: Could not add Tags to Audio File!")
            return

        picture_data = open(picture_file,'rb').read()
        audio.tags.add(APIC(mime='image/png', type=3, desc=u'Cover', data=picture_data))
        audio.save(audio_file)

        audio2 = EasyID3(audio_file)
        audio2['artist'] = artist
        audio2.save()
        
        self.delete_cover(picture_file)

    def delete_cover(self, picture_file) :
        os.remove(picture_file)   