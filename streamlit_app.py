import streamlit as st
import requests
import pandas as pd

import subprocess

api_url = "http://127.0.0.1:5000/api/commits"


@st.cache_data
def fetch_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def start_flask():
    process = subprocess.Popen(['python', 'app.py'])
    return process


flask_process = start_flask()
    

st.title('GitHub - scikit-learn Commits Dashboard')

data = fetch_data()

if data is not None:
    commit_df = pd.DataFrame(data)

    # Display the DataFrame in Streamlit
    st.write(commit_df)
else:
    st.error('Failed to fetch data from the Flask API.')    

