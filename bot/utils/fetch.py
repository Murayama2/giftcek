import requests

def fetch_new_gifts(limit=10):
    url = "https://gifts3.tonnel.network/api/pageGifts"
    payload = {
        "offset": 0,
        "limit": limit,
        "sortBy": "newest"
    }
    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(url, json=payload, headers=headers)
        return res.json().get("gifts", [])
    except:
        return []
