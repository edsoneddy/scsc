a = int(input())
f = ""
for i in range(1, a + 1):  
    c1 = input()
    c2 = ""
    sw = 0
    for k in range(len(c1)):
        if c1[k] == ' ':
            c2 += " "
        else:
            if sw == 0:
                c2 += c1[k].upper()
                sw = 1
            else:
                c2 += c1[k].lower()
                sw = 0
    f += c2 + "\n" 
print(f)
