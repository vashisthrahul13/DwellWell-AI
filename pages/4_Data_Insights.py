import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SWEETVIZ_REPORT_PATH = os.path.join(MAIN_DIR,'4_resources','4.3_sweetviz_report.html')

with open(SWEETVIZ_REPORT_PATH,'r',encoding='utf-8') as html_file:
    html_content = html_file.read()

st.title("Sweetviz Overall Data Insights")
components.html(html_content,height=1000,width=1200,scrolling=True)