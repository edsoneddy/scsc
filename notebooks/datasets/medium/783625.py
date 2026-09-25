def convertir(x):
    s=''
    May= True
    for let in x:
        if let.isalpha():
            if May:
                s+= let.upper()
            else:
                s+= let.lower()
            May = not May
        else:
            s+= let
    return s

m=int(input())
for i in range(m):
    x=str(input())
    print(convertir(x))