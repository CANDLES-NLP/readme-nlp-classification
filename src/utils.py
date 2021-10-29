import json
from numpy import random

def json_repos():
    """Read in JSON trending repos
    """
    with open('2016_trending.json') as f:
        data = json.load(f)
    repos = []
    for l in data:
        for r in data[l]:
            repos.append(r[18:])
    #truncate list
    idx = random.randint(low=0, high=len(data),
                         size=700)
    repos = [repos[i] for i in idx]
    return repos


if __name__ == "__main__":
    data= json_repos()
    print(data, len(data))
