for _ in range(int(input())):
    size = int(input())
    a = input().split()
    b = input().split()
    suma = 0
    for i in range(size):
        suma += int(a[i])*int(b[i])
    print(suma)