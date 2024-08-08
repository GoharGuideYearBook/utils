import gdown
import csv
import os

from PIL import Image

def get_image(file, question_1, question_2):
    pfp_pics = {}
    try:
        with open(file, newline='', encoding="utf-8") as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:
                pfp_pics[row[question_1]] = row[question_2]
    except FileNotFoundError:
        print("No file found!")
        return {}
    
    return pfp_pics

entries = get_image("test.csv", "What's your Discord username?", "Provide your Discord profile picture.")

def download_image(url, save_as):
    gdown.download(url, "images/" + save_as, quiet=False,fuzzy=True)
    image = Image.open("images/" + save_as)
    image.save('images/' + save_as + '.webp', "webp")

    os.remove("images/" + save_as)
    
for entry in entries:
    print(entry + ": " + entries[entry])
    download_image(entries[entry], entry)