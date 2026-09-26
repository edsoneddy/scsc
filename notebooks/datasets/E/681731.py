import sys
import re

def process_input(input_text):
    lines = input_text.split('\n')
    words = []
    current_word = ""
    
    for line in lines:
        line = line.strip()
        if line.endswith('-'):
            current_word += line[:-1]  # Remove trailing hyphen and add to current word
        else:
            current_word += line  # Add the rest of the line to current word
            words.extend(re.sub(r'[^\w-]', ' ', current_word).split())  # Remove punctuation except hyphen, split by spaces, and add to words
            current_word = ""  # Reset current word for the next line
    
    # Convert words to lowercase and remove duplicates
    unique_words = set(word.lower() for word in words)
    
    # Sort words alphabetically
    sorted_words = sorted(unique_words)
    
    return sorted_words

def main():
    input_text = sys.stdin.read()  # Lee toda la entrada hasta EOF
    output_words = process_input(input_text)
    
    for word in output_words:
        print(word)

if __name__ == "__main__":
    main()
