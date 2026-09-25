# Adivine la Estructura
from sys import stdin
from collections import deque
import heapq as pq

for linea in stdin:
    n = int(linea)
    pila = []
    cola = deque([])
    cp = []
    ispila = True
    iscola = True
    iscp = True
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            pila.append(x)
            cola.append(x)
            pq.heappush(cp, -x)
        else:
            if pila.pop() != x:
                ispila = False
            if cola.popleft() != x:
                iscola = False
            if pq.heappop(cp) != -x:
                iscp = False
    p = 1 if ispila else 0
    c = 1 if iscola else 0
    cpr = 1 if iscp else 0
    s = p + c + cpr
    if s == 0:
        print("impossible")
    elif s == 1:
        if p == 1:
            print("stack")
        elif c == 1:
            print("queue")
        else:
            print("priority queue")
    else:
        print("not sure")
