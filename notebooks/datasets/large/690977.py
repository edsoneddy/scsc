import sys
import re

def process_input():
    input_text = sys.stdin.read()
    return input_text

def extract_words(text):
    lines = text.splitlines()
    words = []
    current_word = ""

    for line in lines:
        line = line.strip()
        if line.endswith('-'):
            current_word += line[:-1]
        else:
            current_word += line
            words_in_line = re.findall(r"[a-zA-Z-]+", current_word)
            words.extend(words_in_line)
            current_word = ""

    if current_word:
        words_in_line = re.findall(r"[a-zA-Z-]+", current_word)
        words.extend(words_in_line)

    return words

def main():
    text = process_input()
    words = extract_words(text)
    unique_words = set(word.lower() for word in words)
    sorted_words = sorted(unique_words)

    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
