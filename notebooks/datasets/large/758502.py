import sys
import re

def process_text(lines):
    words_found = set()
    pending_word = ""

    for line in lines:
        if not line.strip():
            continue

        tokens = re.findall(r'[a-zA-Z-]+', line)
        for token in tokens:
            if token.endswith('-') and line.endswith(token):
                pending_word += token[:-1]
            else:
                pending_word += token
                words_found.add(pending_word.lower())
                pending_word = ""

    return sorted(words_found)

def main():
    input = sys.stdin.read
    lines = input().splitlines()
    result = process_text(lines)
    print("\n".join(result))

if __name__ == "__main__":
    main()
