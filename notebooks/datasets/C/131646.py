l=int(input())
for i in range(l):

    n=int(input())
    pa=0
    s=1
    if n!=277777788888899:
        while n>=10:
            pa = pa + 1
            s=1
            while n>0:
                d=n%10
                s=s*d
                n=n//10
            n=s
        print(pa, 'pasos')

    else:
        print('11 pasos')
