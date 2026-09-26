x=int(input())
for i in range(x):
    m=int(input())
    o=m
    c=0
    if m>9:
        while m>9:
            s=1
            while m>0:
                d=m%10
                s=s*d
                m=m//10

            m=s
            c = c + 1
        else:
            print(c,"pasos")
    else:
        print("0 pasos")