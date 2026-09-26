import re

def join_hyphenated_words(text):
    """Join words that are split across lines with hyphens."""
    # Replace hyphen + newline with empty string to join split words
    text = re.sub(r'-\s*\n\s*', '', text)
    return text

def get_unique_words(text):
    """Extract and sort unique words from text."""
    # Convert to lowercase
    text = text.lower()
    
    # Join hyphenated words first
    text = join_hyphenated_words(text)
    
    # Split into words (sequences of letters, preserving hyphens between letters)
    words = re.findall(r'[a-záéíóúñ]+(?:-[a-záéíóúñ]+)*', text)
    
    # Remove duplicates and sort
    unique_words = sorted(set(words))
    
    return unique_words

def main():
    # Read all input until EOF
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    # Join all lines with newlines to preserve line breaks
    text = '\n'.join(lines)
    
    # Get unique words
    unique_words = get_unique_words(text)
    
    # Print each word
    for word in unique_words:
        print(word)

if __name__ == "__main__":
    main()