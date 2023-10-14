# utils.py
import requests


def fetch_data(url, params=None):
    if params is None:
        params = {}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
