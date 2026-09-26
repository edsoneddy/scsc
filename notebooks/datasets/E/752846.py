import sys
import re
word = ''
words = set()
for line in sys.stdin:
    line = line.strip()
    if line.endswith('-'):
        word += line[:-1]
    else:
        word += line
        for w in re.findall(r'[a-zA-Z\-]+', word):
            words.add(w.lower())
        word = ''
for word in sorted(words):
    print(word)