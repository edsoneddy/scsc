num = int(input())
while num >0:
    t = int(input())
    #a = [2, 5, 10, 5, 5, 7, 4, 6, 9, 5]
    #b = [9, 7, 8, 2, 3, 9, 3, 10, 7, 5]
    a = input().split()
    b = input().split()
    interoA=[]
    interoB=[]
    for i in a:
        i = int(i)
        interoA.append(i)
    for j in b:
        j = int(j)
        interoB.append(j)
    #print(interoB,interoA)
    bec = len(a)
    res =[]
    for i in range(bec):
        oper = interoA[i] * interoB[i]
        res.append(oper)
        oper = 0
    print(sum(res))
    num-=1