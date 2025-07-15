import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
sweetviz_report_path= os.path.join(os.path.dirname(__file__), '..', 'resources', 'sweetviz_report.html')

with open(sweetviz_report_path,'r',encoding='utf-8') as html_file:
    html_content = html_file.read()

st.title("Sweetviz Overall Data Insights")
components.html(html_content,height=1000,width=1200,scrolling=True)