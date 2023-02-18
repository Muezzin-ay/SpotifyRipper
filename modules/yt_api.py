
import urllib.request
import yt_dlp

from modules.web_scratch import WebScratch


OUTPUT_LOCATION = './out/'

class YoutubeApi(yt_dlp.YoutubeDL) :
    def __init__(self) -> None:
        ydl_ops = {
            'outtmpl': OUTPUT_LOCATION + '/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
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
        super().download([urls])