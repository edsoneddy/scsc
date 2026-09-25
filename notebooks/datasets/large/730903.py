for _ in range (int(input())):
    n=int(input())
    vector1=list(map(int,input().split()))
    vector2=list(map(int,input().split()))
    if len(vector1)==len(vector2)==n:
        s=0
        for i in range (n):
            s=s+(vector1[i]*vector2[i])
        print (s)