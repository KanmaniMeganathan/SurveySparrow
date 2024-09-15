# SurveySparrow

Developer Performance Analytics Dashboard based on GitHub repository data, designed to provide insights into developer productivity and performance.

Command to start the dashboard

streamlit run .\streamlit_app.py

GitRepoFetch.py 

Fetched data from scikit-learn/scikit-learn repo and save data in commits.csv 

streamlit_app.py

File that has home page of streamlit dashboard, which displays commit data. 
Flask is run as subprocess, in order to run Flask application within a Streamlit project by invoking a separate Python process to run app.py.

query_build.py
query_build file has functionality to handle filter dashboard in streamlit

Pages\filter.py

Dashboard code that inputs data such as author, from date , to date and keyword ( in message) , gives the filtered data which satisfies the conditions fgiven as input. It is not mandatory to input all field.

Pages\frequency.py

Dashboard code- this displays a plot with no of commits in range. It also has option to download commit frequency data.

Pages\sample_openaichat.py

Connecting to GPT with prompt that inputs text from dashboard to convert it into a python query. Later the python query is executed on the commits data and ouptut is displayed.

commits.csv

Dataframe that contains all commits from scikit-learn/scikit-learn repo

Pages\commit_frequency.csv

Dataframe that contains author-wise frequency on no of commits

Pages\commit_frequency_with_ranges.csv

Dataframe that contains author's frequency of commit with range 

