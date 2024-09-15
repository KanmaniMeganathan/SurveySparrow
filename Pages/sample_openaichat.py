import openai
import pandas as pd
import streamlit as st

openai.api_key = "your_openai_api_key"

def generate_query(input_text):
    # Modify the prompt to ensure the query uses 'df' as the DataFrame
    prompt = f"""
    You have a pandas DataFrame named 'df' with the columns sha,author,date,message where each row represents a git commit 
    Generate a Python query to {input_text}. 
    Make sure the DataFrame is referred to as 'df'  and store the result in a variable 'result_df'.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Python code for data analysis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content']

commit_df=pd.read_csv('commits.csv')


#input_text = "give name of authors with frequency of commits more than 2000"
st.title("Chat with me")
input_text=st.text_input("Your Question",value='give name of authors with frequency of commits more than 2000')

query = generate_query(input_text)
exec(query)

if 'result_df' in locals():
    print("Filtered DataFrame:\n", result_df)

st.write(result_df)
