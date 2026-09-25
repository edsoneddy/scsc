def bailarina(c):
    re = ""
    q=""
    sw=1
    for i in range(len(c)):
        if(c[i]==" "):
            re += c[i]
            continue
        else:
            if sw==1:
                re += c[i].upper()
                sw=0
            else:
                re += c[i].lower()
                sw=1
    return re
T = int(input())
for _ in range(T):
    c = input()
    print(bailarina(c))