# Import dependencies
import os
import re
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Helper functions
def initialize_model():
    return genai.GenerativeModel("gemini-pro")

def get_response(model, prompt):
    try:
        return model.generate_content(prompt).text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_video_transcripts(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript])
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_video_id(url):
    patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
        r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]+)',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

# Streamlit app
st.title("YouTube Video Tool")

# Input YouTube video link
youtube_url = st.text_input("Enter YouTube video link:")
video_id = get_video_id(youtube_url) if youtube_url else None

if youtube_url and not video_id:
    st.error("Invalid YouTube URL")

# Display video thumbnail if valid URL
if video_id:
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Option to choose between summary and Q&A
option = st.selectbox("Choose an option", ("Generate Summary", "Ask a Question"))

# Text input for user prompt if the option is "Ask a Question"
user_prompt = st.text_area("Your question based on the video") if option == "Ask a Question" else ""
submit = st.button("Submit")

summary_behavior = """You are an expert in summarizing YouTube videos from transcription of videos. Input is transcription and output will be the summary of the given video including all the important information. Please break down the information into multiple paragraphs if it becomes more clear and concise. Please give a relevant topic for the summary. Please try to make the summary below 1000 words. Please don't add extra information that doesn't make sense but fix typos and return `Couldn't generate summary for the given video` if transcription is meaningless or empty. This is the transcription for the video."""

qa_behavior = """You are an expert in answering questions based on YouTube video transcriptions. Input is transcriptions of videos along with the prompt which has the user's query. Please make sure that you understand all the information present in the video from the transcription and respond to the user's query. Please don't add extra information that doesn't make sense but fix typos and return `Couldn't transcribe the video` if the transcription of the video is empty otherwise respond accordingly!"""

# Handle form submission
if submit and video_id:
    transcriptions = get_video_transcripts(video_id)
    if "An error occurred" in transcriptions:
        st.error(transcriptions)
    else:
        model = initialize_model()
        if option == "Generate Summary":
            prompt = f"{summary_behavior}\n\n{transcriptions}"
            summary = get_response(model, prompt)
            if "Couldn't generate summary" in summary or not summary.strip():
                st.error("Couldn't generate summary for the given video")
            else:
                st.write(summary)
        else:
            prompt = f"{qa_behavior}\nvideo transcription: {transcriptions} \nprompt: {user_prompt}"
            response = get_response(model, prompt)
            if "Couldn't transcribe the video" in response or not response.strip():
                st.error("Couldn't transcribe the video")
            else:
                st.write(response)
