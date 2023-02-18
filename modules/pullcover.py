import urllib.request

import re

class SpotifyCoverLoader():
    def __init__(self) -> None:
        pass

    def get_thumb_url(self):
        pattern = r'loading="eager" src="([^ ]*)"'

        #do not know why, but it works; finds thumbnail url using regex
        req = urllib.request.urlopen('https://open.spotify.com/track/1qsexgIQui6hZ8tAGoEg4G').read().decode('utf-8').encode('cp850','replace').decode('cp850')
        thumbnail_url = re.findall(pattern,req)

        print(thumbnail_url)
        self.thumbnail_url = thumbnail_url[0]

    def download_cover(self):
        print(self.thumbnail_url)
        urllib.request.urlretrieve(self.thumbnail_url,"./out/local-filename.jpg")

        