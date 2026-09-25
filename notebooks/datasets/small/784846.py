from sys import stdin
from math import isqrt
from queue import LifoQueue,PriorityQueue

def input():
    return stdin.readline().strip()

ope=input()
pq=PriorityQueue()

while ope!='T':

    if ope[0]=='S':
        pq.put(-int(ope[2:]))
    else:

        if pq.empty():
            print("Error")
        else:
            if ope=='A':
                num=-pq.get()
                print(num)
                pq.put(-num)
            elif ope=='R':pq.get()
            elif ope[0]=='I':
                num=-pq.get()
                num+=(int(ope[2:]))
                pq.put(-num)
            else:
                num=-pq.get()
                num-=(int(ope[2:]))
                pq.put(-num)


    ope=input()
    

