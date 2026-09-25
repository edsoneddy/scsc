#enteros
n = int(input())
for _ in range(n):
    t = input()
    sw = False
    for c in t :
        if c!= ' ':  
            if sw:
                print(c.lower(), end="")
                sw = False
            else:
                print(c.upper(), end="")
                sw = True
        else:
            print(c, end="")
    print()