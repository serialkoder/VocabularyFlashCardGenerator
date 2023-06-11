# Parse words and meanings from merriam-webster.com
from sys import argv

import requests
from bs4 import BeautifulSoup
import json
import re


# Get the word and meaning from merriam-webster.com
def get_word_meaning(word):
    url = "https://www.merriam-webster.com/dictionary/" + word
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    word = soup.find(class_="hword").get_text()
    meaning = soup.find(class_="dtText").get_text()
    return word, meaning


# Get all meanings from merriam-webster.com
def get_all_meanings(word):
    url = "https://www.merriam-webster.com/dictionary/" + word
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    word = soup.find(class_="hword").get_text()
    meanings = soup.find_all(class_="dtText")
    meanings = [meaning.get_text() for meaning in meanings]
    return word, meanings


# Read from command line argument
word = argv[1]

word, meaning = get_all_meanings(word)

print(word)

for i in range(len(meaning)):
    print(str(i + 1) + ". " + meaning[i])
