T = int(input())
for i in range(T):
    t=1
    bailarina=""
    line = input()
    for caracter in line:
        asc =  ord(caracter)
        if(asc != 32):
            if t == 1:               
                if asc > 90:
                    asc=asc-32
            else:                   
                if asc < 97:
                    asc+=32
        
            t=1-t    
        bailarina+=chr(asc)    
    print(bailarina)