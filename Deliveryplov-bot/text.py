import json

def get_text(key):
    with open("text.json", "r", encoding="utf-8") as f:
        info = json.load(f)
        return info.get(key)