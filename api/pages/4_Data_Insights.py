import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
with open('../api/resources/sweetviz_report.html','r',encoding='utf-8') as html_file:
    html_content = html_file.read()

st.title("Sweetviz Overall Data Insights")
components.html(html_content,height=1000,width=1200,scrolling=True)