import sys
import re

def main():
    input = sys.stdin.read
    lines = input().splitlines()
    unique_words = set()
    temp_word = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        fragments = re.split(r'(?<!-)\s+', line)
        for idx, fragment in enumerate(fragments):
            if fragment.endswith('-') and idx == len(fragments) - 1:
                temp_word += fragment[:-1]
            else:
                temp_word += fragment
                clean_word = re.sub(r'[^a-zA-Z-]', '', temp_word).lower()
                if clean_word:
                    unique_words.add(clean_word)
                temp_word = ""

    for word in sorted(unique_words):
        print(word)

if __name__ == "__main__":
    main()
