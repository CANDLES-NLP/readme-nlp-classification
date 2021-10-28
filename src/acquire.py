from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time
import env

hdr = {"Authorization": f"token {env.token}", "User-Agent": env.username}

def get_repos():
    """Return list of Github repos.
    """
    repos = []
    return repos

def repo_df(repos):
    """Save dataframe of repo READMEs & language.
    """
    repo_data = []         
    return pd.DataFrame(repo_data)

if __name__ == "__main__":
    
    df = repo_df(get_repos())
    df.to_csv('repos.csv', index=0)