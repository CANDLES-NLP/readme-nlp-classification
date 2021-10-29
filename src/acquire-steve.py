from requests import get
import pandas as pd
import env
import utils

#GitHub personal access token and username for use with API
hdr = {'Authorization': f'token {env.github_token}', 'User-Agent': env.github_username}

REPOS = utils.json_repos()

def repo_df():
    """Dataframe with repo, README, & language.
    """
    repo_data = []
    for repo in REPOS:
        url = f'https://api.github.com/repos{repo}'
        try:
            lang = get(url, headers=hdr).json().get('language')
            for file in get(url+'/contents', headers=hdr).json():
                if file['name'].lower().startswith('readme'):
                    rm = get(file['download_url']).text
            repo_data.append({'repo': repo, 'language': lang, 'readme': rm})
        except: continue        
    return pd.DataFrame(repo_data)


if __name__ == "__main__":
    print(REPOS)
    df = repo_df()
    print(f'saving {len(df)} records...\n{df.head()}')
    df.to_csv('repos.csv', index=0)
