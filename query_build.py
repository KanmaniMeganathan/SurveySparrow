import pandas as pd

df = pd.read_csv('commits.csv')

#df['date'] = pd.to_datetime(df['date'])
#df['author'] = df['author'].astype(str)
#df['message'] = df['message'].astype(str)

def build_query(author=None, startdate=None, enddate=None, keyword=None):
    global df

    mask = pd.Series([True] * len(df), index=df.index)
    
    if author:
        mask &= (df['author'] == author)
    if startdate and enddate:
        mask &= (df['date'] >= startdate) & (df['date'] <= enddate)
    elif startdate:
        mask &= (df['date'] >= startdate)
    elif enddate:
        mask &= (df['date'] <= enddate)
    
    query_result = df[mask]

    if keyword:
        query_result = query_result[query_result['message'].str.contains(keyword, case=False)]
    
    return query_result
