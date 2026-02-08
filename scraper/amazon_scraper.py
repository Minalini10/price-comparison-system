from bs4 import BeautifulSoup
import json

# Product data list (easy to extend)
products_data = [
    ("Samsung Galaxy S21", "₹45,999", "https://amazon.in/samsung-galaxy-s21"),
    ("iPhone 13", "₹60,999", "https://amazon.in/iphone-13"),
    ("OnePlus 11", "₹57,499", "https://amazon.in/oneplus-11"),
    ("Redmi Note 12", "₹17,999", "https://amazon.in/redmi-note-12"),
    ("Realme GT Neo 3", "₹36,999", "https://amazon.in/realme-gt-neo-3"),
    ("Vivo V29", "₹32,999", "https://amazon.in/vivo-v29"),
    ("Nothing Phone 2", "₹44,999", "https://amazon.in/nothing-phone-2")
]

products = []

for name, price, link in products_data:
    products.append({
        "platform": "Amazon",
        "name": name,
        "price": price,
        "link": link
    })

print(products)

# Save to JSON
with open("scraper/amazon_output.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("✅ Amazon products saved (multiple items)")
