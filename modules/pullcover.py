import urllib.request
import mutagen
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
        urllib.request.urlretrieve(self.thumbnail_url, f"./out/albumcover.jpg")

    def merge_cover_mp3(self):
        pass
        