a = int(input())
while(a != 0):
    b = int(input())
    lis = []
    lista = []
    m = 0
    for x in map(int, input().split()):
        lis.append(x)
    for y in map(int, input().split()):
        lista.append(y)
    for z in range(1, b + 1):
        m = m + lis[z - 1] * lista[z - 1]
    print(m)
    a = a - 1
    
