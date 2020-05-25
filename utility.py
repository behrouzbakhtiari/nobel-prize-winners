import csv
import requests
import shutil
from shutil import copyfile


def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for j in data:
            writer.writerow(j)


def conver_to_persian_digits(string):
    digits_map = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    return "".join([digits_map[digit] if digit in digits_map.keys() else digit for digit in str(string)])


def download_image(url, path):
    req = requests.get(url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(req.raw, out_file)


def get_template_text(path):
    template_text = ""
    with open(path) as layout:
        template_text = layout.read()
    return template_text
