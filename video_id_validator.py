import validators
import requests
from urllib.parse import urlparse,parse_qs


def get_video_id(video_url):
    if validators.url(video_url):
        try:
            requests.head(video_url,timeout=5,allow_redirects=True)
            a = urlparse(video_url)
            q_a = parse_qs(a.query)
            video_url = video_url
            return q_a.get("v",[None])[0] , video_url
        
        except requests.RequestException:
            return "No such URL exists"
    else:
        return 'not a valid url'