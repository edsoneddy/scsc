c=int(input())
for i in range(c):
    a=int(input())
    l1=input().split()
    l2=input().split()
    s=0
    for j in range(len(l1)):
        s=s+(int(l1[j])*int(l2[j]))
    print(s)