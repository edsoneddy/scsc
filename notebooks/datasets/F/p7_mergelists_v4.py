import heapq

fila1 = input().split()
fila2 = input().split()

n1 = [int(t) for t in fila1]
n2 = [int(t) for t in fila2]

salida = list(heapq.merge(n1, n2))
texto = ""
for i, valor in enumerate(salida):
    if i > 0:
        texto += " "
    texto += str(valor)
print(texto)
