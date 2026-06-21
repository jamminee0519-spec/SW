import streamlit as st
import json
import os

# 파일 저장 경로 설정
DB_FILE = "vocabulary.json"

# 기획서 기반 타이틀
st.title("🤖 AI 자동 인식 스마트 단어장")
st.caption("찍으면 자동으로 채워지고, 똑똑하게 외워지는 단어장")

# --- 탭 구성 (우선순위 Phase 1 기반) ---
tab1, tab2 = st.tabs(["📝 단어 입력 및 저장", "📚 내 단어장 조회"])

# [탭 1] 단어 입력 및 저장
with tab1:
    st.subheader("1. 텍스트 직접 입력")
    user_input = st.text_area("모르는 단어가 포함된 문장이나 단어를 입력하세요.", placeholder="예: Apple은 사과, Banana는 바나나")
    
    if st.button("단어 추출 및 임시 리스트 생성"):
        if user_input.strip():
            st.success("텍스트가 입력되었습니다! (추후 이곳에 AI/OCR 기능이 연동됩니다.)")
            # 임시 데이터 예시
            st.write("**[임시 결과 테이블]**")
            st.code("입력한 내용: " + user_input)
        else:
            st.warning("텍스트를 입력해주세요.")

# [탭 2] 내 단어장 조회
with tab2:
    st.subheader("현재 저장된 단어 목록")
    st.info("아직 저장된 단어가 없습니다. (JSON 파일 연동 예정)")
