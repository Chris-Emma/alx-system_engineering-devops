import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    url = f"https://www.reddit.com/r/CharacterAI/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/Acrobatic_Break4210)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

