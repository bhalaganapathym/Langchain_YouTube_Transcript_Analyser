from video_id_validator import get_video_id
from langchain_core.documents import Document
from youtube_transcript_api import YouTubeTranscriptApi

video_url = input().strip()
video_id, url = get_video_id(video_url=video_url)

api = YouTubeTranscriptApi()

raw = api.fetch(video_id=video_id)

transcript = " ".join([i.text for i in raw])

metadata = {
    "source":"youtube",
    "url" : url
}

doc = Document(page_content=transcript,metadata=metadata)

print((doc.page_content))
