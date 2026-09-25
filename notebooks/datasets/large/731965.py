def multilplicaciónescalar(v1,v2):
    s=0
    for i in range(len(v1)):
        e=v1[i]*v2[i]
        s+=e
    return s

c=int(input())
for i in range(c):
    n=int(input())
    v1=list(map(int,input().split()))
    v2=list(map(int,input().split()))
    print(multilplicaciónescalar(v1,v2))
