# [🎵 J-POP-CrossFade🎤](https://j-pop-crossfade.streamlit.app/)


![iPhone-12-(iOS-14)-j-pop-crossfade streamlit app](https://github.com/user-attachments/assets/cf51bb10-189c-4b39-8541-e1ef239838fa)

## AI 기반의 J-POP ↔️ K-POP 가사 번역 번안 및 각색 도구

> LLM 프롬프팅 기법을 사용하여 언어적, 문화적 차이를 극복하면서도 음악의 본질을 보존합니다.




### 한국어:
AI 기반의 J-POP <--> K-POP 가사 번역 및 각색 도구입니다. LLM 프롬프팅 기법을 사용하여 언어적, 문화적 차이를 극복하면서도 음악의 본질을 보존합니다. 가사의 의미와 운율을 고려한 창의적인 번안으로, 두 문화 간의 음악적 교류를 촉진합니다. 🎵🇯🇵➡️🇰🇷🎤

### 日本語:
J-POP と K-POP の歌詞を相互に翻訳・脚色する AI ベースのツールです。LLM プロンプティング技術を使用し、言語的・文化的な違いを克服しながらも音楽の本質を保ちます。歌詞の意味とリズムを考慮した創造的な翻案により、両文化間の音楽交流を促進します。🎵🇯🇵➡️🇰🇷🎤

### 주요 특징

- 🇯🇵➡️🇰🇷 J-POP에서 K-POP으로 가사 번역
- 🇰🇷➡️🇯🇵 K-POP에서 J-POP으로 가사 번역
- 🎼 운율과 의미를 모두 고려한 창의적 각색
- 🤖 최신 AI 기술 활용

### 사용 방법

1. J-POP 또는 K-POP 가사 입력
2. 번역 방향 선택
3. '번역 및 각색' 버튼 클릭
4. AI가 생성한 결과 확인

### 지원 언어

| 입력 | 출력 |
|------|------|
| 일본어 | 한국어 |
| 한국어 | 일본어 |

```python
from jpop_crossfade import translate_and_adapt_lyrics

# 입력 가사 (Kenshi Yonezu - "Kick Back")
input_lyrics = """
そう無邪気なチャイムが鳴る
なにもない日々の行進曲
影を連れて行こう
どこへ向かおうか
響くキックバック
"""

print("노래 정보:")
print("제목: Kick Back")
print("가수: 요네즈 켄시 (米津玄師)")
print("발매년도: 2022")
print("비고: 애니메이션 'Chainsaw Man' 오프닝 테마")

print("\n원본 가사:")
print(input_lyrics)

# 번역 및 음운 유사성을 고려한 의역 수행
result = translate_and_adapt_lyrics(input_lyrics, source="ja", target="ko", phonetic_similarity=0.7)

print("\n한국어 번역:")
print(result['translation'])

print("\n음운 유사성을 고려한 K-POP 스타일 의역:")
print(result['adaptation'])

# 출력 예시:
# 노래 정보:
# 제목: Kick Back
# 가수: 요네즈 켄시 (米津玄師)
# 발매년도: 2022
# 비고: 애니메이션 'Chainsaw Man' 오프닝 테마
#
# 원본 가사:
# そう無邪気なチャイムが鳴る
# なにもない日々の行進曲
# 影を連れて行こう
# どこへ向かおうか
# 響くキックバック
#
# 한국어 번역:
# 그래 순진한 차임벨이 울린다
# 아무것도 없는 나날의 행진곡
# 그림자를 데리고 가자
# 어디로 향할까
# 울려 퍼지는 킥백
#
# 음운 유사성을 고려한 K-POP 스타일 의역:
# 소박한 차임이 울려
# 공허한 나날의 행진곡
# 그림자 데려 가볼까
# 어디로 갈까 우리
# 킥백 소리 울려
```


```python
from jpop_crossfade import translate_and_adapt_lyrics

# 입력 가사 (YOASOBI - "夜に駆ける(Yoru ni Kakeru)")
input_lyrics = """
駆け抜けてく 未来へと
僕らの足を止めるものなど何もない
"""

print("노래 정보:")
print("제목: 夜に駆ける (밤을 달리다)")
print("가수: YOASOBI")
print("발매년도: 2019")

print("\n원본 가사:")
print(input_lyrics)

# 번역 및 의역 수행
result = translate_and_adapt_lyrics(input_lyrics, source="ja", target="ko")

print("\n한국어 번역:")
print(result['translation'])

print("\nK-POP 스타일 의역:")
print(result['adaptation'])

# 출력 예시:
# 노래 정보:
# 제목: 夜に駆ける (밤을 달리다)
# 가수: YOASOBI
# 발매년도: 2019
#
# 원본 가사:
# 駆け抜けてく 未来へと
# 僕らの足を止めるものなど何もない
#
# 한국어 번역:
# 달려나가네 미래를 향해
# 우리의 발을 멈추게 할 것 따위 아무것도 없어
#
# K-POP 스타일 의역:
# 달려가자 내일을 향해
# 우리 앞길 가로막을 순 없어
```

**J-POP-CrossFade**로 음악의 경계를 넘어 새로운 창작의 세계를 경험하세요! 🌟
