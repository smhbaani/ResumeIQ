import json
import os


def load_json(filepath):

    with open(filepath, "r") as file:
        return json.load(file)


def save_text_report(content, filepath):

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)


def percentage(part, total):

    if total == 0:
        return 0

    return round((part / total) * 100, 2)


def safe_get(data, key):

    return data.get(key, "Not Available")