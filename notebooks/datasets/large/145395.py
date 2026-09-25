casos=int(input())
while casos > 0:
    casos=casos-1
    x=int(input())
    s=0
    l1=[int(x) for x in input().split()]
    l2=[int(y) for y in input().split()]
    for t in range(x):
       s=s+l1[t]*l2[t]
    print(s)