n = int(input())

for i in range(n):
    num = int(input())
    v1 = list(map(int,input().split()))
    v2 = list(map(int, input().split()))
    suma = 0
    for h in range(num):
        suma = suma + v1[h]*v2[h]
    print(suma)