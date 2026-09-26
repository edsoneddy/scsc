def bailarin(text):
    new = ''
    c = 0
    for letra in text:
        if ord(letra) != 32:
            if c %2 ==0:
                new += letra.upper()
                c+=1
            else:
                new += letra.lower()
                c+=1
        else:
            new += ' '    
        
    return new
    
case = int(input())
for _ in range(case):
    t = input()
    print(bailarin(t))