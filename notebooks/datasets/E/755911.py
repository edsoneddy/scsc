def texto():
    palabras = set()  
    pendiente = ""  
    
    try:
        while True:
            try:
                line = input().strip()
                
               
                if not line and pendiente:
                    palabras.add(pendiente.lower())
                    pendiente = ""
                    continue
                
              
                actual = line.split()
                
                if not actual:
                    continue
                    
               
                for i, word in enumerate(actual):
                    
                    word = word.rstrip('.,')
                    
                    
                    if pendiente:
                        if word.endswith('-'):
                         
                            pendiente += word[:-1]
                        else:
                    
                            completo = pendiente + word
                            palabras.add(completo.lower())
                            pendiente = ""
                    
                    
                    elif word.endswith('-'):
                        if i == len(actual) - 1:  
                            pendiente = word[:-1]
                        else:
                           
                            palabras.add(word.lower())
                    
                    
                    else:
                       
                        if any(c.isalpha() for c in word):
                            palabras.add(word.lower())
                
            except EOFError:
               
                if pendiente:
                    palabras.add(pendiente.lower())
                break
    
   
        fin = set()
        for word in palabras:
            if '-' in word and not word.endswith('-'):
               
                fin.add(word)
                fin.add(word.replace('-', ''))
            else:
                fin.add(word)
        
        
        for word in sorted(fin):
            print(word)
            
    except EOFError:
        pass


texto()