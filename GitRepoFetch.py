from github import Github
import pandas as pd

token ="your github token"
g = Github(token)
repo = g.get_repo("scikit-learn/scikit-learn")

commits = repo.get_commits()

commit_data = []
for commit in commits:
    commit_data.append({
        "sha": commit.sha,
        "author": commit.author.login if commit.author else "Unknown",
        "date": commit.commit.author.date,
        "message": commit.commit.message
    })

commit_df = pd.DataFrame(commit_data)
commit_df.to_csv('commits.csv', index=False)



