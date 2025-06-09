import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find(id="productTitle")
    price = soup.find("span", class_="a-offscreen")
    return {
        "name": title.get_text(strip=True) if title else "Ürün adı bulunamadı",
        "price": price.get_text(strip=True) if price else "Fiyat bulunamadı",
        "satisfaction": 85,
        "risk": 10,
        "aura": 80,
        "expert_score": 88
    }
