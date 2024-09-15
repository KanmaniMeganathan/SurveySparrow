import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read commits data
commit_df = pd.read_csv('commits.csv')

# Calculate commit frequency per developer
commit_frequency = commit_df.groupby('author').size().reset_index(name='commit_count')

# Sort by commit count for better display
commit_frequency = commit_frequency.sort_values(by='commit_count', ascending=False)

# Define new commit count ranges to accommodate higher values
bins = [0, 50, 100, 200, 500, 1000, 2000, commit_frequency['commit_count'].max() + 1]
labels = ['0-50', '51-100', '101-200', '201-500', '501-1000', '1001-2000', '2000+']

# Bin the commit counts
commit_frequency['range'] = pd.cut(commit_frequency['commit_count'], bins=bins, labels=labels, right=False)

# Count the number of developers in each range
range_counts = commit_frequency['range'].value_counts().sort_index()

# Streamlit app
st.title('Commit Frequency Analysis')
# Plotting with counts above bars
st.subheader('Number of Developers by Commit Count Range')

plt.figure(figsize=(12, 8))
bars = plt.bar(range_counts.index, range_counts.values, color='skyblue')

# Add counts above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # X position
        height,  # Y position
        f'{int(height)}',  # Text to display
        ha='center',  # Horizontal alignment
        va='bottom',  # Vertical alignment
        fontsize=10
    )

plt.xlabel('Commit Count Range')
plt.ylabel('Number of Developers')
plt.title('Number of Developers by Commit Count Range')
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(plt)

# Save the CSV file in the current directory
csv_file_path = 'commit_frequency_with_ranges.csv'
commit_frequency.to_csv(csv_file_path, index=False)

# Provide download button
with open(csv_file_path, 'rb') as file:
    st.download_button(
        label="Download commit frequency CSV",
        data=file,
        file_name='commit_frequency_with_ranges.csv',
        mime='text/csv'
    )


# Display the frequency table
st.subheader('Frequency of Commits per Developer')
commit_frequency_no_range = commit_frequency.drop(columns=['range'])
st.dataframe(commit_frequency_no_range)
