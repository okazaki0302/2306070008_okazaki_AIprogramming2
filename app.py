import streamlit as st
from logic import fetch_wikipedia_summary

st.set_page_config(page_title="Wikipedia要約アプリ", layout="centered")

st.title("📚 Wikipedia要約アプリ")
st.write("キーワードを入力すると、Wikipediaの要約を表示します。")

keyword = st.text_input("🔍 キーワードを入力してください", "")

if keyword:
    result = fetch_wikipedia_summary(keyword)
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader(result["title"])
        st.write(result["summary"])
        st.markdown(f"[🔗 Wikipediaページへ]({result['url']})")
