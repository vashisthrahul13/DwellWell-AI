import streamlit as st

file_path = "readme.md"
with open(file_path, "r", encoding="utf-8") as file:
    markdown_content = file.read()

st.markdown(markdown_content,unsafe_allow_html=True)