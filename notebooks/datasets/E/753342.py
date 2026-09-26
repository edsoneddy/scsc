def process_text():
    words = set() 
    pending_word = ""  
    
    try:
        while True:
            try:
                line = input().strip()
      
                if not line and pending_word:
                    words.add(pending_word.lower())
                    pending_word = ""
                    continue
       
                current_words = line.split()
                
                if not current_words:
                    continue
      
                for i, word in enumerate(current_words):
                    word = word.rstrip('.,')
     
                    if pending_word:
                        if word.endswith('-'):
                            pending_word += word[:-1]
                        else:
                            complete_word = pending_word + word
                            words.add(complete_word.lower())
                            pending_word = ""
 
                    elif word.endswith('-'):
                        if i == len(current_words) - 1: 
                            pending_word = word[:-1]
                        else:
                            words.add(word.lower())
 
                    else:
                        if any(c.isalpha() for c in word):
                            words.add(word.lower())
                
            except EOFError:
                if pending_word:
                    words.add(pending_word.lower())
                break
 
        final_words = set()
        for word in words:
            if '-' in word and not word.endswith('-'):
                final_words.add(word)
                final_words.add(word.replace('-', ''))
            else:
                final_words.add(word)
       
        for word in sorted(final_words):
            print(word)
            
    except EOFError:
        pass

process_text()