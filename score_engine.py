def generate_scorecard(product):
    return f"""
📌 {product['name']}
💸 {product['price']}
✅ Tatmin: {product.get('satisfaction', 'N/A')}
🧯 Risk: {product.get('risk', 'N/A')}
💠 Hissiyat: {product.get('aura', 'N/A')}
⚙️ Uzman Test: {product.get('expert_score', 'N/A')}
"""
