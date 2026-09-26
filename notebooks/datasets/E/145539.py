re =int(input())
while re >0:
    inu = input()
    c = input().split()
    d = input().split()
    lsd =[]
    a = []
    b = []
    tama = len(c)
    for i in c:

        gegi= int(i)
        a.append(gegi)
    for i in d:

        gego= int(i)
        b.append(gego)
    for i in range(tama):
        multis = a[i] * b[i]
        lsd.append(multis)
    print(sum(lsd))
    re-=1