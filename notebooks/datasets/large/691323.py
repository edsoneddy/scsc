from sys import stdin, stdout
from collections import deque
from queue import PriorityQueue
for i in stdin:
    if i=="\n":
        break
    n = int(i)
    pila = []
    cola = deque([])
    prioritycola = PriorityQueue()
    swPila = True
    swCola = True
    swPC = True
    for i in range(n):
        a, b = map(int,stdin.readline().split())
        if a==1:
            pila.append(b)
            cola.append(b)
            prioritycola.put(-b)
        else:
            if pila.pop() != b:
                swPila = False
            if cola.popleft() != b:
                swCola = False
            if -prioritycola.get() != b:
                swPC = False
    if (swPila and swCola) or (swPila and swPC) or (swCola and swPC):
        stdout.write(str("not sure")+"\n")
    elif swPila:
        stdout.write(str("stack")+"\n")
    elif swCola:
        stdout.write(str("queue")+"\n")
    elif swPC:
        stdout.write(str("priority queue")+"\n")
    else:
        stdout.write(str("impossible")+"\n")