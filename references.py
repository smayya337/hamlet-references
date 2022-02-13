# Detect references to Shakespeare's *Hamlet* using a Jaccard index.

from nltk.stem import WordNetLemmatizer
import re
import sys

scenes = []
lemmatized_lines = []
lines = []

with open("hamlet_lemmatized.txt") as fil:
    for line in fil:
        pieces = line.split("    ")
        scenes.append(pieces[0])
        lemmatized_lines.append(pieces[1])

with open("hamlet.txt") as fil:
    for line in fil:
        pieces = line.split("    ")
        lines.append(pieces[1])

scenes_to_lines = {scene: list() for scene in set(scenes)}
for i, line in enumerate(lines):
    actual_lines = line.split("\t")
    for actual_line in actual_lines:
        scenes_to_lines[scenes[i]].append(actual_line.strip())

valid_chars = re.compile(r"[A-Za-z0-9 ]")
lemmatizer = WordNetLemmatizer()

quote = sys.argv[1].strip()
lemmatized_quote = "".join([c for c in quote if valid_chars.match(c)])
quote_set = {word for word in lemmatized_quote.split()}
lemmatized_sets = [{word for word in line.split()} for line in lemmatized_lines]

match_levels = sorted(
    [(len(quote_set.intersection(match)) / (len(quote_set.intersection(match)) + len(quote_set) + len(match)), i) for
     i, match in enumerate(lemmatized_sets)], reverse=True)
best_match = match_levels[0][1]

print("Closest match:")
print("\"" + lines[best_match].replace("\t", "\n").strip() + "\"")
match_act = scenes[best_match].split(".")[0]
match_scene = scenes[best_match].split(".")[1]
start_line = lines[best_match].split("\t")[0].strip()
end_line = lines[best_match].split("\t")[-1].strip()
start_line_index = scenes_to_lines[scenes[best_match]].index(start_line) + 1
end_line_index = scenes_to_lines[scenes[best_match]].index(end_line) + 1
line_string = f"lines {start_line_index} - {end_line_index}" if start_line_index != end_line_index else f"line {start_line_index}"
print(f"Act {match_act}, scene {match_scene}, {line_string}")
print(f"Jacard index: {match_levels[0][0]}")
