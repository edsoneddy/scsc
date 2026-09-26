import heapq

numeros = []
while True:
    operacion = input().split()
    if operacion[0] == 'T':
        break
    elif operacion[0] == 'S':
        heapq.heappush(numeros, -int(operacion[1]))
    elif operacion[0] == 'A':
        if numeros:
            print(-numeros[0])
        else:
            print('Error')
    elif operacion[0] == 'R':
        if numeros:
            heapq.heappop(numeros)
        else:
            print('Error')
    elif operacion[0] == 'I':
        if numeros:
            maximo = -heapq.heappop(numeros)
            maximo += int(operacion[1])
            heapq.heappush(numeros, -maximo)
        else:
            print('Error')
    elif operacion[0] == 'D':
        if numeros:
            maximo = -heapq.heappop(numeros)
            maximo -= int(operacion[1])
            heapq.heappush(numeros, -maximo)
        else:
            print('Error')
