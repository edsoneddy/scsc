n = int(input())
for i in range(1, n+1):
    cad = input(); baile = ""; sw = 0 
    for i in range(0, len(cad)):
        if (cad[i] == ' '):
            baile = baile + cad[i]
        else:
            if (sw == 0):
                baile = baile + cad[i].upper()
                sw = 1
            else:
                baile = baile + cad[i].lower()
                sw = 0
    print(baile)