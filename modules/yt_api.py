
import urllib.request
import yt_dlp

from modules.web_scratch import WebScratch


class YoutubeApi :

    def __init__(self, output_location) :
        self.output_location = output_location

    def search_song(self, song) :
        search_word = song.get_search_word()
        search_url = f'https://www.youtube.com/results?search_query={search_word}'

        video_urls = []
        try :
            html = urllib.request.urlopen(search_url)
            html_source = html.read().decode()
            video_urls = WebScratch.gen_video_urls(html_source)
        except UnicodeEncodeError as err:
            return err
        
        return self.choose_url(video_urls, song)
        
    def choose_url(self, urls, song) :
        try :
            for video_counter, url in enumerate(urls) :
                html = urllib.request.urlopen(url)
                html_source = html.read().decode()

                if WebScratch.verify_video(html_source, song) :
                    print(f"[YOUTUBE-API] Using video number {video_counter+1} ( {url} ).")
                    return url

        except Exception as err:
            print(err)

        return urls[0]
        
    def download(self, urls, song) :
        ydl_ops = {
            'outtmpl': self.output_location + song.get_file_name(),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        dlp = yt_dlp.YoutubeDL(ydl_ops)
        dlp.download(urls)