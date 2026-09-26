import sys

def input():
    return sys.stdin.readline().strip()

n=int(input())
for i in range(n):
    size=int(input())
    vec1=list(map(int,input().split()))
    vec2=list(map(int,input().split()))
    res=0
    for j in range(size):
        res+=(vec1[j]*vec2[j])
    print(res)