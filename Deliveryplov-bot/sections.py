import json
from telegram import ReplyKeyboardMarkup

main_section = ReplyKeyboardMarkup([
    ["☎️ Biz bilan aloqa", "🛍 Buyurtma berish"],
    ["✍️ Fikr bildirish", "⚙️ Sozlamalar"]
], resize_keyboard = True)

with open('products.json', 'r', encoding='utf-8') as f:
    all_products = json.load(f)

product_section = ReplyKeyboardMarkup([
    *[list(all_products.keys())[i:i + 2] for i in range(0, len(all_products), 2)],
    ["Asosiyga qaytish"]
], resize_keyboard = True)