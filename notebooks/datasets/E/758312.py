import sys
import re

def process_words(text):
    # Convert all text to lowercase
    text = text.lower()
    
    # Replace hyphens at the end of lines with empty string
    text = re.sub(r'-\s*\n', '', text)
    
    # Replace newlines with spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Split text into words
    words = re.findall(r'\b[a-z-]+\b', text)
    
    # Remove duplicates and sort
    unique_words = sorted(set(words))
    
    return unique_words

# Read input until EOF
input_text = sys.stdin.read()

# Process the input and get unique words
result = process_words(input_text)

# Print the result
for word in result:
    print(word)