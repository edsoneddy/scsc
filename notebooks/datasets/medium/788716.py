t = int(input())
for _ in range(t):
    cad = input()
    cad2 = ""
    sw = True
    for i in range(len(cad)):
        if ord(cad[i]) != 32:
            if sw:
                cad2 = cad2 + cad[i].upper()
                sw = False
                
            else:
                cad2 = cad2 + cad[i].lower()
                sw = True
        else:
            cad2 = cad2 + " "
    print(cad2)