# A helper script to download and format the script of *Hamlet*.


from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
import re
import requests

HAMLET_URL = "http://shakespeare.mit.edu/hamlet/full.html"
HAMLET_HTML = requests.get(HAMLET_URL).text
# print(HAMLET_HTML)
soup = BeautifulSoup(HAMLET_HTML, "html.parser")

blockquotes = soup.find_all("blockquote")  # The text of the play is in "blockquote -> a" elements
lines = []
lemmatized_lines = []
scenes = []
valid_chars = re.compile(r"[A-Za-z0-9 ]")
lemmatizer = WordNetLemmatizer()
for i, quote in enumerate(blockquotes):
    children = quote.findChildren("a")
    if not children:
        continue
    scene = ".".join(children[0].get("name").split(".")[:2])
    scenes.append(scene)
    initialtext = ""
    lemmatized_initialtext = ""
    for child in children:
        section = child.text
        lemmatized_section = "".join([c for c in child.text if valid_chars.match(c)])
        initialtext += section.strip()
        initialtext += "\t"
        lemmatized_initialtext += lemmatized_section
        lemmatized_initialtext += " "
    lines.append(initialtext.strip())
    fulltext = ""
    for word in lemmatized_initialtext.split():
        fulltext += lemmatizer.lemmatize(word)
        fulltext += " "
    lemmatized_lines.append(fulltext.strip().lower())
print(lines)

with open("hamlet.txt", "w") as fil:
    for i, line in enumerate(lines):
        fullline = scenes[i] + "    " + line.strip()
        fil.write(fullline + "\n")

with open("hamlet_lemmatized.txt", "w") as fil:
    for i, line in enumerate(lemmatized_lines):
        fullline = scenes[i] + "    " + line.strip()
        fil.write(fullline + "\n")
