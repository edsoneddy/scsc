t = int(input())
while t > 0:
    cad = input()
    cad2 = ""
    sw = 0
    for i in range(len(cad)):
        if cad[i] != ' ':
            if sw == 0:
                cad2 += cad[i].upper()
                sw = 1
            else:
                cad2 += cad[i].lower()
                sw = 0
        else:
            cad2 += ' '

    print(cad2)
    t -= 1
