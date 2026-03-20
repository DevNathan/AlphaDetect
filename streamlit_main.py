import streamlit as st
import joblib
import pandas as pd
from collections import Counter

LANG_MAP = {
    "en": "영어 (English)",
    "fr": "프랑스어 (French)",
    "id": "인도네시아어 (Indonesian)",
    "tl": "타갈로그어 (Tagalog)"
}

@st.cache_resource
def load_model():
    return joblib.load('lang_detect_model.pkl')

# 사전에 학습된 분류기 모델 로드
clf = load_model()

def process_text(text: str) -> tuple:
    text = text.lower()
    counter = Counter(text)
  
    cnt = [counter[chr(i + ord('a'))] for i in range(26)]
    total = sum(cnt)
    
    if total == 0:
        return None, None
      
    freq = [n / total for n in cnt]
    
    pred = clf.predict([freq])
    detected_lang = LANG_MAP.get(pred[0], "알 수 없는 언어")
    
    return detected_lang, freq

# UI 구성
st.set_page_config(page_title="AlphaDetect", layout="centered")

st.title("AlphaDetect")
st.markdown("**Lightweight language detection engine based on alphabet frequency.**")
st.markdown("텍스트를 입력하면 알파벳 DNA를 분석하여 언어를 판별합니다.")

user_input = st.text_area("분석할 텍스트를 입력하십시오:", height=200)

if st.button("분석 실행 (Analyze)"):
    if not user_input.strip():
        st.warning("텍스트를 입력해 주십시오.")
    else:
        with st.spinner("알파벳 DNA 스캔 중..."):
            detected_lang, freq_data = process_text(user_input)
            
            if detected_lang is None:
                st.error("유의미한 영문 알파벳이 존재하지 않습니다.")
            else:
                st.success("분석 완료")
                st.subheader(f"판별 결과: **{detected_lang}**")
                
                st.markdown("---")
                st.markdown("### 추출된 알파벳 빈도수 (Language DNA)")
                
                alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
                df_freq = pd.DataFrame({"Frequency": freq_data}, index=alphabets)
                
                st.bar_chart(df_freq)
