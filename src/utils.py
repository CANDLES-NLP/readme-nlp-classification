import json

def json_repos():
    """Read in JSON repos and cutoff at 106 per langauge
    """
    with open('2016_trending.json') as f:data = json.load(f)
    repos = []
    for l in data:
        if len(data[l]) < 100 or l=='None':
            continue
        for ix, r in enumerate(data[l]):
            repos.append(r[18:])
            if ix > 105: break
    return repos


if __name__ == "__main__":
    data = json_repos()
    print(data[:5], len(data))
