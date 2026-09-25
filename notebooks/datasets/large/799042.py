L = input()
c = int(L)
for k in range(c):
    n = int(input())
    A = input().split()
    B = input().split()
    suma = 0
    for i in range(n):
        valA = int(A[i])
        valB = int(B[i])
        suma = suma + (valA * valB)
    print(suma)