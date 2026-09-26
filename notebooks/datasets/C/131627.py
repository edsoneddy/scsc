n=int(input())
for i in range(n):
    j=int(input())
    c=0
    if j>=10:
        while j>=10:
            m=1
            while j>0:
                d=j%10
                m=m*d
                j=j//10

            j=m
            c=c+1
        else:
            print(c,"pasos")
    else:
        print("0 pasos")