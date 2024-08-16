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

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

def translate_and_adapt_lyrics(lyrics, sim_weight, mean_weight):
    prompt = f"""
    작업: J-Pop 가사를 K-Pop 스타일로 변환하되, 음운적 유사성({sim_weight})과 의미 보존({mean_weight})의 균형을 맞추세요.

    원본 J-Pop 가사:
    {lyrics}

    지침:
    1. 일본어 가사의 직역을 한국어로 제공하세요.
    2. 다음 지침을 따라 K-Pop 스타일로 각색하세요:
       - 원래 일본어와의 음운적 유사성 유지 (가중치: {sim_weight})
       - 원래 의미 보존 (가중치: {mean_weight})
       - 각색된 가사가 원곡의 멜로디에 맞고 부르기 쉬운지 확인
       - 현재 K-Pop 트렌드와 인기 있는 표현 포함
       - 문화적 맥락을 고려하고 적절히 조정
    3. 각 줄마다 다음을 제공하세요:
       a) 원본 일본어
       b) 직역 한국어
       c) K-Pop 스타일 각색 (한국어)
       d) 각색 선택에 대한 설명
    4. 다음 음악적 요소를 고려하세요:
       - 원곡의 리듬과 강세 패턴
       - 음절 수와 배치
       - 고음이나 지속음을 위한 모음 소리
    5. K-Pop 시장에 맞는 창의적인 재해석을 적절히 추가하세요

    출력 형식:
    1번 줄:
    원본 (일본어): [일본어]
    직역: [한국어 번역]
    K-Pop 각색: [각색된 한국어]
    설명: [각색 선택, 문화적 고려사항, 음악적 요소에 대한 간단한 설명]

    [각 줄마다 반복]

    전체 각색 전략:
    [소리와 의미의 균형, K-Pop 트렌드 반영, 문화적 조정 등 전반적인 접근 방식 설명]

    K-Pop 시장 고려사항:
    [이 각색이 K-Pop 팬들에게 어떻게 어필할 수 있고 현재 트렌드에 맞는지 논의]

    잠재적 도전 과제:
    [각색하기 특히 어려운 줄이나 개념을 식별하고 어떻게 해결했는지 설명]

    최종 K-Pop 각색:
    [완성된 K-Pop 각색 가사를 한국어로 제공]

    기억하세요: 목표는 한국어로 자연스럽게 들리고, 원곡의 본질을 유지하며, 원곡의 멜로디에 맞춰 부를 수 있고, K-Pop 시장에 어필할 수 있는 K-Pop 가사를 만드는 것입니다.
    """

    response = model.generate_content(prompt)
    return response.text

def vocal_score(j_pop_lyrics, k_pop_lyrics):
    prompt = f"""
    당신은 강력한 보컬과 다양한 언어의 노래를 적응시키는 능력으로 유명한 전설적인 K-Pop 록스타입니다. 당신의 임무는 원래의 J-Pop 가사와 비교하여 K-Pop 번안 버전의 부르기 쉬운 정도를 평가하는 것입니다. 각 라인의 흐름, 리듬, 그리고 얼마나 부르기 쉬운지에 집중하세요.

    원래 J-Pop 가사:
    {j_pop_lyrics}

    K-Pop 번안 가사:
    {k_pop_lyrics}

    각 라인 쌍에 대해 다음을 제공하세요:
    1. 부르기 쉬운 정도에 대한 간단한 비교
    2. 1-10점 척도의 "보컬 점수" (10점이 부르기에 가장 완벽한 상태)
    3. 록스타 스타일의 짧고 캐주얼한 코멘트 (슬랭을 사용하고, 표현력 있게!)

    출력 형식 예시:
    라인 1:
    J-Pop: [일본어 가사]
    K-Pop: [한국어 가사]
    비교: [간단한 분석]
    보컬 점수: [1-10]
    록스타 코멘트: [캐주얼하고 슬랭이 가득한 코멘트]

    전체 요약:
    [번안 버전의 부르기 쉬운 정도에 대한 간단한 전체 평가]
    총 보컬 점수: [모든 라인 점수의 평균]
    최종 록스타 평가: [록스타 스타일의 전체 의견]

    기억하세요, 당신은 록스타입니다! 자신감 있게, 음악 슬랭을 사용하고, 코멘트에 약간의 엣지를 주는 것을 두려워하지 마세요. 이 평가를 록킹하자! 🎸🤘
    """

    response = model.generate_content(prompt)
    return response.text

def jpop_to_kpop_with_evaluation(j_pop_lyrics, similarity_weight, meaning_weight):
    # 번역 및 각색 수행
    adaptation_result = translate_and_adapt_lyrics(j_pop_lyrics, similarity_weight, meaning_weight)
    
    # 결과에서 원본 일본어 가사와 최종 K-Pop 가사 추출
    # 참고: 이 부분은 실제 출력 형식에 따라 조정이 필요할 수 있습니다
    j_pop_lyrics_extracted = "원본 일본어 가사"  # adaptation_result에서 추출
    k_pop_lyrics_extracted = "최종 K-Pop 각색 가사"  # adaptation_result에서 추출

    # 보컬 점수 평가 수행
    vocal_evaluation = vocal_score(j_pop_lyrics_extracted, k_pop_lyrics_extracted)

    # 최종 결과 조합
    final_result = f"""
    번역 및 각색 결과:
    {adaptation_result}

    보컬 점수 평가:
    {vocal_evaluation}
    """

    return final_result

# Streamlit UI
st.set_page_config(page_title="J-POP-CrossFade", layout="wide", page_icon=favicon)

# CSS 스타일
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    body {
        background-color: #F5F5DC;
        color: #8B0000;
        font-family: 'Pretendard', sans-serif;
    }
    .title {
        color: #8B0000;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        font-family: 'Pretendard', sans-serif;
    }
    .subtitle {
        color: #8B4513;
        font-size: 24px;
        text-align: center;
        font-family: 'Pretendard', sans-serif;
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
        font-family: 'Pretendard', sans-serif;
    }
    .text-input {
        background-color: #FFFFF0;
        border: 1px solid #8B0000;
        color: #8B4513;
        font-family: 'Pretendard', sans-serif;
    }
    .output-text {
        background-color: #FFFFF0;
        border: 1px solid #8B0000;
        color: #8B4513;
        padding: 10px;
        border-radius: 5px;
        font-family: 'Pretendard', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# 제목과 부제목
st.markdown('<p class="title">J-POP-CrossFade</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI 기반 J-Pop to K-Pop 가사 번역기 및 평가기</p>', unsafe_allow_html=True)

jpop_examples = {
    "YOASOBI - 夜に駆ける (Yoru ni Kakeru)": """
    駆け抜けてく 未来へと
    僕らの足を止めるものなど何もない
    強くなれる 理由を知った
    僕を連れて進め
    """,

    "Official HIGE DANdism - Pretender": """
    君とのラブストーリー
    それは予想通り
    いざ始まればひとり芝居だ
    ずっとそばにいたって
    結局ただの観客だ
    """,

    "米津玄師 (Kenshi Yonezu) - Lemon": """
    夢ならばどれほどよかったでしょう
    未だにあなたのことを夢にみる
    忘れた物を取りに帰るように
    古びた思い出の埃を払う
    """,

    "あいみょん (Aimyon) - マリーゴールド (Marigold)": """
    さよならを言えなかった
    引き止めることもできなかった
    もう二度と会えないってわかっていたのに
    二人で見た映画のラストシーン
    君は泣いていて 僕も泣いていた
    """,

    "LiSA - 紅蓮華 (Gurenge)": """
    強くなれる理由を知った
    僕を連れて進め
    泥だらけの走馬灯に酔う
    こわばる心超えて
    来たる日を想う
    """,

    "King Gnu - 白日 (Hakujitsu)": """
    まぶしい光を浴びて
    君は少し眠そうだ
    僕が見つめてたその横顔
    永遠を感じてた
    """,

    "菅田将暉 (Suda Masaki) - 見たこともない景色 (Mita Koto mo nai Keshiki)": """
    誰かの為に生きるのは
    誰かの為に生きられる人だけ
    僕はただ君を守りたいだけ
    それ以上でもそれ以下でもない
    """,

    "back number - 高嶺の花子さん (Takane no Hanako-san)": """
    ねぇ 今でも覚えてる?
    あの日の事 君の事
    たまに思い出しては
    今も胸が痛くなるよ
    """,

    "優里 (Yuuri) - ドライフラワー (Dry Flower)": """
    君の好きな歌を
    歌っていたら涙が出てきた
    思い出すなよって
    頭の中で自分に言い聞かせた
    """,

    "Mrs. GREEN APPLE - インフェルノ (Inferno)": """
    目を覚ませ 僕の中で眠る獣よ
    目覚めし時 何も恐れず 突き進め
    闇を抜けたその先に
    光射す未来がある
    """
}


# 메인 영역
col1, col2 = st.columns(2)

with col1:
    st.subheader("원본 J-Pop 가사")
    # 여기에 예시 선택 및 입력 필드 추가
    example_selection = st.selectbox(
        "예시 가사 선택 (또는 직접 입력)",
        ["직접 입력"] + list(jpop_examples.keys())
    )

    if example_selection == "직접 입력":
        j_pop_lyrics = st.text_area("일본어 가사를 입력하세요", height=200, key="input")
    else:
        j_pop_lyrics = st.text_area("일본어 가사를 입력하세요", value=jpop_examples[example_selection], height=200, key="input")

with col2:
    st.subheader("번역 설정")
    similarity_weight = st.slider("음운적 유사성 가중치", 0.0, 1.0, 0.5, key='similarity')
    meaning_weight = st.slider("의미 보존 가중치", 0.0, 1.0, 0.5, key='meaning')

if st.button("번역, 각색 및 평가", key="translate"):
    if j_pop_lyrics:
        result = jpop_to_kpop_with_evaluation(j_pop_lyrics, similarity_weight, meaning_weight)
        st.markdown(f'<div class="output-text">{result}</div>', unsafe_allow_html=True)
    else:
        st.warning("번역을 시작하기 전에 J-Pop 가사를 입력해주세요.")


# 푸터
st.markdown("---")
st.markdown("Developed with ❤️ by Purang2")
