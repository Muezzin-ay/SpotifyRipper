
import re


URL_PATTERN = r"watch\?v=(\S{11})"
DURATION_PATTERN = r'<meta itemprop="duration" content="PT(\d+)M(\d+)S">'


class WebScratch :
    def __init__(self) -> None:
        pass

    def gen_video_urls(self, html_source) :
        video_urls = []
        try :
            video_ids = re.findall(URL_PATTERN, html_source)
            for i in range(10) : #Max Search Resulst -> 10
                video_url = "https://www.youtube.com/watch?v=" + video_ids[i]
                video_urls.append(video_url)
            return video_urls
        except :
            return None
        
    def extract_duration(self, html_source) :
        try :
            duration_data = re.findall(DURATION_PATTERN, html_source)[0]
        except :
            return None
        duration = int(duration_data[0]) * 60 + int(duration_data[1])
        return duration
    
    