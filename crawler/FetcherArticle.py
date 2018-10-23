import requests
from bs4 import BeautifulSoup
import time
import csv
import os.path


class ArticleFetcher:
    def __init__(self, url, directory, filename):
        self.url = url
        self.directory = directory
        self.filename = filename

    def fetch(self):
        print("URL: " + self.url)
        print("DIRECTORY: " + self.directory)
        print("FILENAME: " + self.filename)
        time.sleep(1)
        r = requests.get(self.url)
        doc = BeautifulSoup(r.text, "html.parser")
        completepath = os.path.join(self.directory + "/", self.filename + ".csv")
        print("SAVED FILE TO: " + completepath)

        tweetlist = []
        readlist = []

        with open(completepath, "w", newline="", encoding="utf-8"):
            pass  # just opening of new file

        for element in doc.select(".content"):
            tweetlist.append(element.select_one(".js-tweet-text-container").text.strip())

        with open(completepath, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter="*")
            for row in reader:
                readlist.append(row[0])

        for tweet in tweetlist:
            if tweet in readlist:
                pass
            else:
                readlist.append(tweet)

        with open(completepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter="*")
            for entry in readlist:
                writer.writerow([entry])

        print(str(len(readlist)) + " TWEETS SAVED TO " + str(completepath))
