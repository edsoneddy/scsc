import sys
import re

def main():
    text = sys.stdin.read() 
    words = []
    current_word = ""

    
    for line in text.splitlines():
        line = line.strip() 
        
     
        if line.endswith('-'):
            current_word += line[:-1]  
        else:
            current_word += line
            words.extend(re.findall(r"[a-zA-Z-]+", current_word))
            current_word = ""  

   
    words = list(set(word.lower() for word in words))
    
    
    words.sort()
    

    for word in words:
        print(word)

if __name__ == "__main__":
    main()
