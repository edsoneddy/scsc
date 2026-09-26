n = int(input())
for i in range(n):
    cad = input()
    res = ""
    s1,s2 = 0,0
    for j in range(len(cad)):
        if(cad[j] != ' '):
            if(s1 == 0):
                res = res + cad[j].upper()
                s1 = 1
                s2 = 0
            elif(s2 == 0):
                res = res + cad[j].lower()
                s2 = 1
                s1 = 0
        else:
            res = res + ' '  
    print(res)
            
