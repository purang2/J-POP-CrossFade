import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

genai.configure(api_key=st.secrets["gemini"])
# 이미지 파일 로드
favicon = Image.open('images/favicon.png')

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')

# Function to translate lyrics using Gemini
def translate_lyrics(lyrics, similarity_weight, meaning_weight):
    prompt = f"""
    Task: J-Pop to K-Pop lyrics translation and adaptation

    Original J-Pop lyrics:
    {lyrics}

    Instructions:
    1. Translate the given Japanese lyrics to Korean.
    2. Adapt the translation to maintain a similar sound and rhythm to the original, with a weight of {similarity_weight}.
    3. Ensure the meaning is preserved as much as possible, with a weight of {meaning_weight}.
    4. The result should be suitable for singing in Korean.

    Please provide:
    1. Direct translation
    2. Phonetically similar adaptation
    3. Final version balancing sound and meaning
    4. Brief explanation of your adaptation process
    """

    response = model.generate_content(prompt)
    return response.text

# Streamlit UI code (mostly unchanged)
st.set_page_config(page_title="J-POP-CrossFade", layout="wide", page_icon=favicon)

# (CSS styles remain the same)

st.markdown('<p class="title">J-POP-CrossFade</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered J-Pop to K-Pop Lyrics Translator using Gemini Pro 1.5</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original J-Pop Lyrics")
    japanese_lyrics = st.text_area("Enter Japanese lyrics here", height=200, key="input")

with col2:
    st.subheader("Translated K-Pop Lyrics")
    if st.button("Translate and Adapt", key="translate"):
        similarity_weight = st.session_state.get('similarity', 0.5)
        meaning_weight = st.session_state.get('meaning', 0.5)
        translated_lyrics = translate_lyrics(japanese_lyrics, similarity_weight, meaning_weight)
        st.markdown(f'<div class="output-text">{translated_lyrics}</div>', unsafe_allow_html=True)

# Translation history (remains the same)

# Sidebar: Translation Settings
st.sidebar.header("Translation Settings")
similarity = st.sidebar.slider("Phonetic Similarity", 0.0, 1.0, 0.5, key='similarity')
meaning = st.sidebar.slider("Semantic Accuracy", 0.0, 1.0, 0.5, key='meaning')
