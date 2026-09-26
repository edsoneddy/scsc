import sys
import re

def main():
    unique_words = set()  # Use a set to avoid duplicates
    line_buffer = ""  # Buffer to store lines ending with a hyphen

    for line in sys.stdin:
        trimmed_line = line.rstrip()  # Remove trailing whitespace
        if trimmed_line.endswith('-'):
            line_buffer += trimmed_line[:-1]  # Add line without hyphen
        else:
            line_buffer += trimmed_line  # Add complete line
            # Split words in the buffer
            for word in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', line_buffer):
                unique_words.add(word.lower())  # Add lowercase word to set
            line_buffer = ""  # Clear the buffer

    # If there's content in the buffer after the last line
    if line_buffer:
        for word in re.findall(r'\b\w[\w-]*\w\b|\b\w\b', line_buffer):
            unique_words.add(word.lower())

    # Convert the set to a sorted list
    sorted_words = sorted(unique_words)

    # Print each word on a new line
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
