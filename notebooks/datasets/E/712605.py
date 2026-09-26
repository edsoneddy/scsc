def process_text():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    words = set()
    current_word = ""
    
    for line in data:
        if line.endswith('-'):
            current_word += line[:-1]
        else:
            current_word += line
            cleaned_words = [word.rstrip('.,') for word in current_word.lower().split()]
            words.update(cleaned_words)
            current_word = ""
    
    if current_word:
        cleaned_words = [word.rstrip('.,') for word in current_word.lower().split()]
        words.update(cleaned_words)
    
    sorted_words = sorted(words)
    
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    process_text()
