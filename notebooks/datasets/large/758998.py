import sys
import re
 
def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    words = set()
    current_word = ""
 
    for line in data:
       
        line = line.strip()
        if not line:
            continue
 
       
        parts = re.split(r'(?<!-)\s+', line)
        for i, part in enumerate(parts):
            if part.endswith('-') and i == len(parts) - 1:
                current_word += part[:-1] 
            else:
                current_word += part
                word = re.sub(r'[^a-zA-Z-]', '', current_word).lower()
                if word:
                    words.add(word)
                current_word = ""
 
    for word in sorted(words):
        print(word)
 
if __name__ == "__main__":
    main()
