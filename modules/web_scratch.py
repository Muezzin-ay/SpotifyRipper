import re


URL_PATTERN = r"watch\?v=(\S{11})"


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

    