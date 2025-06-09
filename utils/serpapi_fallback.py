import os
import requests

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_product_on_google(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    return {
        "name": query,
        "price": "N/A",
        "satisfaction": 70,
        "risk": 20,
        "aura": 70,
        "expert_score": 75
    }
