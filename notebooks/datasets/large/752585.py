import sys
import re

lines = sys.stdin.read().splitlines()

words = []
buffer = ""

for line in lines:
    line = line.strip()
    if line.endswith('-') and len(line) > 1:  
        buffer += line[:-1]  
    else:
        buffer += line
        buffer = re.findall(r"[a-zA-Z\-]+", buffer) 
        words.extend(buffer)
        buffer = "" 


unique_words = sorted(set(word.lower() for word in words))


for word in unique_words:
    print(word)
