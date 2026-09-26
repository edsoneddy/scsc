for _ in range(int(input())):
    cad = input()
    boo = True
    newcad = ""
    for i in cad:
        if(i == ' '):
            newcad =newcad + i
        elif(boo):
            if(ord(i) >= 65 and ord(i) <= 90):
                newcad =newcad + i
            else:
                newcad = newcad + chr(ord(i)-32)
            boo = False
        else:
            if(ord(i) >= 97 and ord(i) <= 122):
                newcad =newcad + i
            else:
                newcad = newcad + chr(ord(i)+32)
            boo = True
        
    print(newcad)
