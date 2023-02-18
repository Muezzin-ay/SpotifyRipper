
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

        video_urls = []
        try :
            print(search_url)
            html = urllib.request.urlopen(search_url)
            html_source = html.read().decode()
            video_urls = self.scratch.gen_video_urls(html_source)
        except UnicodeEncodeError as err:
            return err
        
        return self.choose_url(video_urls, song)
        
    def choose_url(self, urls, song) :
        try :
            video_counter = 0
            for url in urls :
                video_counter += 1

                html = urllib.request.urlopen(url)
                html_source = html.read().decode()
                duration = self.scratch.extract_duration(html_source)

                if not duration : #if duration == None
                    continue

                if song.check_duration(duration) :
                    print(f"[YOUTUBE-API] Using video number {video_counter} ({url}).")
                    return url

        except Exception as err:
            print(err)

        return urls[0]
        
    def download(self, urls) :
        super().download(urls)