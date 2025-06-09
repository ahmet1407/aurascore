from flask import Flask, request
from scraper_router import scrape_link
from score_engine import generate_scorecard
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/message", methods=["POST"])
def message():
    incoming_msg = request.get_data(as_text=True)
    logging.info(f"📩 Gelen mesaj: {incoming_msg}")
    try:
        product_data = scrape_link(incoming_msg)
        scorecard = generate_scorecard(product_data)
        return scorecard
    except Exception as e:
        logging.error(f"❌ WhatsApp mesajı hatası: {str(e)}")
        return "Bir hata oluştu."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
