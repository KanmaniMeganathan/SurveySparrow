import streamlit as st
import pandas as pd

from query_build import build_query

st.title("Filter Data by Conditions")

col1,col2 = st.columns(2)
author = col1.text_input("Author",value='agramfort')
keyword = col1.text_input("keyword",value='lasso')
startdate = col2.text_input("From",value='2010-03-03')
enddate = col2.text_input("To",value='2010-04-10')

query_result = build_query(author, startdate, enddate, keyword)

st.write("Fetched Results")
st.write(query_result)
