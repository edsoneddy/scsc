import sys
import re

def process_text():
    words = []
    continuation = ""

    for line in sys.stdin:
        line = line.strip()
        if continuation:
            line = continuation + line
            continuation = ""
        if line.endswith('-'):
            continuation = line[:-1]
            continue
        words.extend(re.findall(r'[a-zA-Z-]+', line))

    if continuation:
        words.append(continuation)

    return sorted(set(word.lower() for word in words))

for word in process_text():
    print(word)
