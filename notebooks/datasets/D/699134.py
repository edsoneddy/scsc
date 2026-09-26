for j in range(int(input())):
    a = input().lower()
    b = ""
    c = True
    for i in range(len(a)):
        if(a[i] != " "):
            if(c):
                c = False
                b += a[i].upper()
            else:
                c = True
                b += a[i].lower()
        else:
            b += " "
    print(b)
