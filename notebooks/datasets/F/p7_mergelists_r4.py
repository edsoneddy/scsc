import heapq

def combinar(x, y):
    return list(heapq.merge(x, y))

primera = list(map(int, input().split()))
segunda = list(map(int, input().split()))
resultado = combinar(primera, segunda)
texto = ' '.join(map(str, resultado))
print(texto)
