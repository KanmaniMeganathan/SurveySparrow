import pandas as pd

df = pd.read_csv('commits.csv')

#df['date'] = pd.to_datetime(df['date'])
#df['author'] = df['author'].astype(str)
#df['message'] = df['message'].astype(str)

def build_query(author=None, startdate=None, enddate=None, keyword=None):
    global df

    # Start with a mask that is True for all rows
    mask = pd.Series([True] * len(df), index=df.index)
    
    # Apply conditions to the mask
    if author:
        mask &= (df['author'] == author)
    if startdate and enddate:
        mask &= (df['date'] >= startdate) & (df['date'] <= enddate)
    elif startdate:
        mask &= (df['date'] >= startdate)
    elif enddate:
        mask &= (df['date'] <= enddate)
    
    # Apply the mask to filter the DataFrame
    query_result = df[mask]

    # Apply keyword filtering if specified
    if keyword:
        query_result = query_result[query_result['message'].str.contains(keyword, case=False)]
    
    return query_result