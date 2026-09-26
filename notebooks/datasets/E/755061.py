import sys
import re
def process_text():
    input_lines = sys.stdin.read().splitlines()  
    words = []
    current_word = ""
 
    for line in input_lines:
        line = line.strip()
        if line.endswith("-"): 
            current_word += line[:-1]  
        else:
            current_word += line 
            words.extend(re.findall(r"[a-zA-Z-]+", current_word)) 
            current_word = ""  
    unique_words = sorted(set(word.lower() for word in words))
    print("\n".join(unique_words))
 
if __name__ == "__main__":
    process_text()