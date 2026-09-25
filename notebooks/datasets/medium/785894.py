a=input()

for i in range(int(a)):
    b=input()
    nuevo=""
    sw = True
    for x in b:

        if(x!=" "):
            if(sw):
                nuevo+=x.upper()
            else:
                nuevo+=x.lower()
            sw=not sw
        else:
            nuevo+=" "
    print(nuevo)