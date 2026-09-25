import sys
import re
 
def main():
   
    input_lines = sys.stdin.read().splitlines()
    
    
    combined_text = " ".join(input_lines)
    
    
    processed_text = re.sub(r"-\s+", "", combined_text)
    
   
    words = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)?", processed_text)
    
   
    words = [word.lower() for word in words]
    
    
    unique_words = set(words)
    
    
    sorted_words = sorted(unique_words)
    
   
    for word in sorted_words:
        print(word)
 
if __name__ == "__main__":
    main()
    #O(n + m log m)