def conv(char):
    sw=True
    cad=""
    for i in char:
        if i!=' ':
            if sw:
                cad+=i.upper()
                sw=False
            else:
                sw=True
                cad+=i.lower()
        else:
            cad+=i
    return cad

t=int(input())
for i in range(t):
    char=input()
    print(conv(char))