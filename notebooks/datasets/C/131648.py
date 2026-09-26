nc = int(input())
c = 0
s = 11
for i in range (0,nc):
    c = 0
    n = int(input())
    while(n>=9):
        m = 1
        while(n>0):
            m=n%10*m
            n=n//10
        n=m
        c = c+1
    print(c, 'pasos')