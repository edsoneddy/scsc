casos=int(input())
for i in range(casos):
    prod = 0
    numero = int(input())
    a = [0] * numero
    a = input().split()
    b = [0] * numero
    b = input().split()
    for j in range(numero):
        prod = prod + int(a[j]) * int(b[j])
    print(prod)
