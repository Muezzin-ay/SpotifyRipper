from song import Song
from web_scratch import WebScratch

import urllib.request
import youtube_dl


class YoutubeApi(youtube_dl.YoutubeDL) :
    def __init__(self) -> None:
        ydl_ops = {
            #'outtmpl':  f'/{TEMP_DIR}/{video_title}.mp4',
            'format': 'bestvideo[width<=720]+bestaudio[ext=m4]/best'
        }
        super().__init__(ydl_ops)

        self.scratch = WebScratch()

    def search_song(self, song) :
        search_word = song.get_search_word()
        search_url = f'https://www.youtube.com/results?search_query={search_word}'
        try :
            html = urllib.request.urlopen(search_url)
            html_source = html.read().decode()
            video_urls = self.scratch.gen_video_urls(html_source)

            return video_urls
        
        except UnicodeEncodeError as err:
            return err
        
    def download(self, urls) :
        super().download([urls[0]])
        


if __name__ == '__main__' : 
    yt = YoutubeApi()
    song = Song("come2gether", "ooyy", 5000)

    urls = yt.search_song(song)
    print(urls)
    yt.download(urls[0])