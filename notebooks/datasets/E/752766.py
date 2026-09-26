import sys
import re

def main():
    words = set() 
    current_word = ""  
    
    
    for line in sys.stdin:
        
        line = line.strip()
        
        
        words_in_line = line.split()
        
        for word in words_in_line:
            
            word = re.sub(r'[^a-zA-Z-]', '', word).lower() 
            
            
            if word.endswith('-'):
                current_word += word[:-1] 
            else:
                if current_word:
                    current_word += word 
                    words.add(current_word)  
                    current_word = "" 
                else:
                    words.add(word)  
    
    
    if current_word:
        words.add(current_word)
    
    
    for word in sorted(words):
        print(word)


if __name__ == "__main__":
    main()
