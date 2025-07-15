#!/bin/bash

# Start Uvicorn in the background
uvicorn app:app --host 0.0.0.0 --port 8000 --reload &

# Start Streamlit
streamlit run Home_Page.py --server.port 8501

