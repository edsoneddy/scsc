from collections import deque

datos = input().split()
cola = deque()

for texto in datos:
    cola.appendleft(int(texto))

print(" ".join(str(x) for x in cola))
