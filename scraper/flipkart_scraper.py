import json

# Flipkart product list (easy to add more)
products_data = [
    ("Samsung Galaxy S21", "₹44,999", "https://flipkart.com/samsung-galaxy-s21"),
    ("iPhone 13", "₹59,999", "https://flipkart.com/iphone-13"),
    ("OnePlus 11", "₹56,999", "https://flipkart.com/oneplus-11"),
    ("Redmi Note 12", "₹16,999", "https://flipkart.com/redmi-note-12"),
    ("Realme GT Neo 3", "₹35,999", "https://flipkart.com/realme-gt-neo-3"),
    ("Vivo V29", "₹31,999", "https://flipkart.com/vivo-v29"),
    ("Nothing Phone 2", "₹43,999", "https://flipkart.com/nothing-phone-2")
]

products = []

for name, price, link in products_data:
    products.append({
        "platform": "Flipkart",
        "name": name,
        "price": price,
        "link": link
    })

print(products)

# Save to JSON
with open("scraper/flipkart_output.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print("✅ Flipkart products saved (multiple items)")
