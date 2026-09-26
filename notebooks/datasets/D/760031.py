n = int(input())
for i in range(n + 1):
    c = input().lower()
    s = ''
    cont = 0
    for j in range(len(c)):
        if c[j] == ' ':
            s = s + c[j]
        else:
            if cont % 2 == 0:
                s = s + c[j].upper()
                cont = cont + 1
            else:
                s = s + c[j]
                cont = cont + 1
    print(s)