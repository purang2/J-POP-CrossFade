import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="J-POP-CrossFade", layout="wide")

# CSS 스타일 정의
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

# 타이틀과 서브타이틀
st.markdown('<p class="title">J-POP-CrossFade</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-powered J-Pop to K-Pop Lyrics Translator</p>', unsafe_allow_html=True)

# 메인 영역
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original J-Pop Lyrics")
    japanese_lyrics = st.text_area("Enter Japanese lyrics here", height=200, key="input")

with col2:
    st.subheader("Translated K-Pop Lyrics")
    if st.button("Translate and Adapt", key="translate"):
        # 여기에 실제 번역/번안 로직이 들어갑니다.
        translated_lyrics = f"This is a K-Pop adaptation of '{japanese_lyrics}'"
        st.markdown(f'<div class="output-text">{translated_lyrics}</div>', unsafe_allow_html=True)

# 하단 영역: 플레이리스트 유사 기능
st.markdown("---")
st.subheader("Translation History")

# 더미 데이터로 히스토리 표시
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

# 하단 버튼
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Previous", key="prev")
with col2:
    st.button("Next", key="next")
with col3:
    st.button("Clear History", key="clear")

# 사이드바: 설정
st.sidebar.header("Translation Settings")
st.sidebar.slider("Phonetic Similarity", 0.0, 1.0, 0.5)
st.sidebar.slider("Semantic Accuracy", 0.0, 1.0, 0.5)
st.sidebar.selectbox("Translation Style", ["Literal", "Adaptive", "Creative"])
