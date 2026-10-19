########################################
#            MODULE IMPORT             #
########################################

from video_id_validator import get_video_id

########################################
#        LANGCHAIN_ESSENTIALS          #
########################################

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.prompts import ChatPromptTemplate

####################################
#     YOUTUBE TRANSCRIPT API       #
####################################
from youtube_transcript_api import YouTubeTranscriptApi

###########################
#     ENV LOADER          #
###########################


from dotenv import load_dotenv
load_dotenv()


video_url = input().strip()
video_id, url = get_video_id(video_url=video_url)

######################################
#               LLM                  #
######################################
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")



prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Summarize the following transcript section.
                    Give:
                    - Main ideas
                    - Key takeaways
                    - Important concepts
            """
        ),
        (
            "human",
            {trs}
        )
    ]
)

chain = prompt | llm

#######################################
#       TRANSCRIPT EXTRACTION         #
#######################################

api = YouTubeTranscriptApi()
raw = api.fetch(video_id=video_id)
transcript = " ".join([i.text for i in raw])

metadata = {
    "source":"youtube",
    "url" : url
}

################################################
#           CONVERSION TO DOCUMENT             #
################################################

doc = Document(page_content=transcript,metadata=metadata)


################################################
#              DOCUMENT TO CHUNKS              #
################################################


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents([doc])



