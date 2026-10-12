from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

video_id = input().strip()

raw = api.fetch(video_id,preserve_formatting=False,languages=["en"])

f = " ".join([e.text for e in raw])

print(f)