from utils.detect_platform import detect_platform
from utils.scrape_amazon import scrape_amazon_product
from utils.scrape_hepsiburada import scrape_hepsiburada_product
from utils.scrape_trendyol import scrape_trendyol_product
from utils.serpapi_fallback import search_product_on_google

def scrape_link(link_or_query):
    platform = detect_platform(link_or_query)
    if platform == "amazon":
        try:
            return scrape_amazon_product(link_or_query)
        except:
            return search_product_on_google(link_or_query)
    elif platform == "hepsiburada":
        try:
            return scrape_hepsiburada_product(link_or_query)
        except:
            return search_product_on_google(link_or_query)
    elif platform == "trendyol":
        try:
            return scrape_trendyol_product(link_or_query)
        except:
            return search_product_on_google(link_or_query)
    else:
        return search_product_on_google(link_or_query)
