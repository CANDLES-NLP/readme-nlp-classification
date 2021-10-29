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
                         size=500)
    repos = [repos[i] for i in idx]
    return repos


if __name__ == "__main__":
    print(json_repos())
