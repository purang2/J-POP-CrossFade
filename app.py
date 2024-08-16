import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
import datetime
import json
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
    
    Task: Transform J-Pop lyrics into K-Pop style, balancing phonetic similarity ({similarity_weight}) and meaning preservation ({meaning_weight})

    Original J-Pop lyrics:
    {j_pop_lyrics}

    Instructions:
    1. Provide a direct Korean translation of the Japanese lyrics.
    2. Create a K-Pop style adaptation following these guidelines:
       - Maintain phonetic similarity to the original Japanese (weight: {similarity_weight})
       - Preserve the original meaning (weight: {meaning_weight})
       - Ensure the adapted lyrics fit the original melody and are singable
       - Incorporate current K-Pop trends and popular expressions
       - Consider the cultural context and make appropriate adjustments
    3. For each line, provide:
       a) Original Japanese (with romaji)
       b) Direct Korean translation
       c) K-Pop style adaptation (with romaji)
       d) Explanation of your adaptation choices
    4. Consider these musical elements:
       - Rhythm and stress patterns of the original
       - Syllable count and placement
       - Vowel sounds for high notes or sustained notes
    5. Add creative reinterpretations where appropriate to suit the K-Pop market

    Output format:
    Line 1:
    Original (JP): [Japanese] / [Romaji]
    Direct Translation: [Korean translation]
    K-Pop Adaptation: [Adapted Korean] / [Romaji]
    Explanation: [Brief explanation of adaptation choices, cultural considerations, and musical elements]

    [Repeat for each line]

    Overall Adaptation Strategy:
    [Explain your overall approach, including how you balanced sound and meaning, incorporated K-Pop trends, and made cultural adjustments]

    K-Pop Market Considerations:
    [Discuss how this adaptation might appeal to K-Pop fans and fit current trends]

    Potential Challenges:
    [Identify any particularly difficult lines or concepts to adapt, and how you addressed them]

    Remember: The goal is to create K-Pop lyrics that sound natural in Korean, maintain the essence of the original, could be sung to the original melody, and appeal to the K-Pop market.
    
    """

    response = model.generate_content(prompt)
    return response.text

# Streamlit UI code
st.set_page_config(page_title="J-POP-CrossFade", layout="wide",page_icon=favicon)

# CSS styles
st.markdown("""
<style>
    body {
        background-color: #F5F5DC;
        color: #8B0000;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #8B0000;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #8B4513;
        font-size: 24px;
        text-align: center;
    }
    .button {
        background-color: #8B0000;
        color: #FFFFF0;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .text-input {
        background-color: #FFFFF0;
        border: 1px solid #8B0000;
        color: #8B4513;
    }
    .output-text {
        background-color: #FFFFF0;
        border: 1px solid #8B0000;
        color: #8B4513;
        padding: 10px;
        border-radius: 5px;
    }
    .song-item {
        background-color: #FFFFF0;
        border: 1px solid #8B0000;
        color: #8B4513;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">J-POP-CrossFade</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered J-Pop to K-Pop Lyrics Translator using Gemini Pro 1.5</p>', unsafe_allow_html=True)

# Main area
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

# Translation history
st.markdown("---")
st.subheader("Translation History")

# Dummy data for history display
history = [
    {"original": "上を向いて歩こう", "translated": "고개를 들고 걸어가자"},
    {"original": "幸せなら手をたたこう", "translated": "행복하다면 손뼉을 치자"},
    {"original": "チェリー", "translated": "체리"}
]

for item in history:
    col1, col2, col3 = st.columns([3,3,1])
    with col1:
        st.markdown(f'<div class="song-item">{item["original"]}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="song-item">{item["translated"]}</div>', unsafe_allow_html=True)
    with col3:
        st.button("Retry", key=f"retry_{random.randint(1,1000)}")

# Bottom buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Previous", key="prev")
with col2:
    st.button("Next", key="next")
with col3:
    st.button("Clear History", key="clear")

# Sidebar: Translation Settings
st.sidebar.header("Translation Settings")
similarity = st.sidebar.slider("Phonetic Similarity", 0.0, 1.0, 0.5, key='similarity')
meaning = st.sidebar.slider("Semantic Accuracy", 0.0, 1.0, 0.5, key='meaning')
