
import urllib.request
import yt_dlp

from modules.web_scratch import WebScratch


OUTPUT_LOCATION = './out/'

class YoutubeApi() :

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
            video_counter = 0
            for url in urls :
                video_counter += 1

                html = urllib.request.urlopen(url)
                html_source = html.read().decode()
                duration =WebScratch.extract_duration(html_source)

                if not duration : #if duration == None
                    continue

                if song.check_duration(duration) :
                    print(f"[YOUTUBE-API] Using video number {video_counter} ( {url} ).")
                    return url

        except Exception as err:
            print(err)

        return urls[0]
        
    def download(self, urls, name) :
        ydl_ops = {
            'outtmpl': OUTPUT_LOCATION + name,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        dlp = yt_dlp.YoutubeDL(ydl_ops)
        dlp.download(urls)