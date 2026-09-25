for _ in range(int(input())):
    x = input()
    cad = ""
    switch=1; mayus=1; minu=2
    for i in range(len(x)):
        char = ord(x[i])
        if((char >= 65 and char <= 90) or (char >= 97 and char <= 122)):
            if(mayus == switch):
                if(char>= 97 and char <= 122):
                    char = char -32
                cad = cad + chr(char);switch=2
            elif(minu == switch):
                if(char >= 65 and char <= 90):
                    char = char +32
                cad = cad + chr(char) ; switch = 1
        else:
            cad = cad + chr(char)
    print(cad)
    
    
