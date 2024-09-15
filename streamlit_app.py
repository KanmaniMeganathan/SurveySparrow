import streamlit as st
import requests
import pandas as pd

import subprocess

# Flask API URL
api_url = "http://127.0.0.1:5000/api/commits"

# Fetch data from Flask API
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

# Start Flask server
flask_process = start_flask()
    
# Display data in the Streamlit dashboard
st.title('GitHub - scikit-learn Commits Dashboard')

data = fetch_data()

if data is not None:
    commit_df = pd.DataFrame(data)

    # Display the DataFrame in Streamlit
    st.write(commit_df)
else:
    st.error('Failed to fetch data from the Flask API.')    

