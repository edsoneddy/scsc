t = int(input())  

for _ in range(t):
    n = int(input())  
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    producto = 0
    for i in range(n):
        producto += A[i] * B[i]

    print(producto)
