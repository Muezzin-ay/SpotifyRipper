
import re

from modules.name_tools import NameTools


URL_PATTERN = r"watch\?v=(\S{11})"
DURATION_PATTERN = r'<meta itemprop="duration" content="PT(\d+)M(\d+)S">'
VIDEO_NAME_PATTERN = r'<title>(.*)</title><meta'


class WebScratch :

    @staticmethod
    def gen_video_urls(html_source) :
        video_urls = []
        try :
            video_ids = re.findall(URL_PATTERN, html_source)
            for i in range(10) : #Max Search Resulst -> 10
                video_url = "https://www.youtube.com/watch?v=" + video_ids[i]
                video_urls.append(video_url)
            return video_urls
        except :
            return None
        
    @staticmethod    
    def extract_duration(html_source) :
        try :
            duration_data = re.findall(DURATION_PATTERN, html_source)[0]
        except :
            return None
        duration = int(duration_data[0]) * 60 + int(duration_data[1])
        return duration
    
    @staticmethod
    def extract_video_name(html_source) :
        try :
            name = re.findall(VIDEO_NAME_PATTERN, html_source)[0]
            return NameTools.gen_comparable_name(name)
        except :
            return None
    
    @staticmethod
    def verify_video(html_source, song) :
        duration = WebScratch.extract_duration(html_source)
        if not duration :
            return False
        
        keyword_name = NameTools.gen_comparable_name(song.name)
        keyword_video_name = WebScratch.extract_video_name(html_source)

        if song.check_duration(duration) :
            if (keyword_name not in keyword_video_name) :
                print(f"[Scratch] Titeltest nicht bestanden, maybe the output is bad! Compared '{keyword_name}' and '{keyword_video_name}'")
            else :
                print("[Scratch] Titeltest bestanden!")
            return True
        
        return False