import sys
import re
 
def main():
    words = set()
    buffer = ""
 
    for line in sys.stdin:
        line = line.rstrip()
 
        if buffer:
            line = buffer + line
            buffer = ""
 
        if line.endswith("-"):
            buffer = line[:-1]
            continue
 
        matches = re.findall(r"[a-zA-Z\-]+", line)
        for word in matches:
            words.add(word.lower())
 
    for word in sorted(words):
        print(word)
 
if __name__ == "__main__":
    main()