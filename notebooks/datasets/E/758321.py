import sys
import re

def main():
    dictionary = set()  
    current_word = []   

    for line in sys.stdin:
        parts = line.split()  

        for i, word in enumerate(parts):
            if word.endswith("-") and i < len(parts) - 1:
                current_word.append(word[:-1])  
            elif word.endswith("-"):
                current_word.append(word[:-1])
            else:
                current_word.append(word)
                final_word = ''.join(current_word).lower()
                final_word = re.sub(r"[^a-z-]", "", final_word)
                if final_word:
                    dictionary.add(final_word)
                current_word = [] 
    for word in sorted(dictionary):
        print(word)

if __name__ == "__main__":
    main()
