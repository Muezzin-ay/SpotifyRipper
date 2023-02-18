import urllib.request
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3
import re

class SpotifyCoverLoader():
    def __init__(self, album_url) -> None:
        pattern = r'loading="eager" src="([^ ]*)"'

        #do not know why, but it works; finds thumbnail url using regex
        req = urllib.request.urlopen(album_url).read().decode('utf-8').encode('cp850','replace').decode('cp850')
        thumbnail_url = re.findall(pattern,req)

        print(thumbnail_url)
        self.thumbnail_url = thumbnail_url[0]

    def download_cover(self):
        print(self.thumbnail_url)
        urllib.request.urlretrieve(self.thumbnail_url, "./out/albumcover.jpg")

    def merge_cover(self, file_name):
        audio_file = f"./out/{file_name}.mp3"
        picture_file = "./out/albumcover.jpg"

        audio = MP3(audio_file, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass

        picture_data = open(picture_file,'rb').read()
        audio.tags.add(APIC(mime='image/png', type=3, desc=u'Cover', data=picture_data))
        audio.save(audio_file)
        
        