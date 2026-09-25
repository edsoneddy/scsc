from collections import deque
import heapq

def D(Y):
    S, Q, P = [], deque(), []  # stack, queue, priority queue
    couldBeStack, couldBeQueue, couldBePq = True, True, True
    R = []
    
    for O, X in Y:
        if O == 1:  # insertar
            S.append(X)
            Q.append(X)
            heapq.heappush(P, -X)
        else:  # op == 2, extraer
            R.append(X)
            if S and S[-1] != X: couldBeStack = False
            if S: S.pop()
            if Q and Q[0] != X: couldBeQueue = False
            if Q: Q.popleft()
            if P and -heapq.heappop(P) != X: couldBePq = False
    
    possible = sum([couldBeStack, couldBeQueue, couldBePq])
    if possible == 0: return "impossible"
    if possible > 1: return "not sure"
    if couldBeStack: return "stack"
    if couldBeQueue: return "queue"
    return "priority queue"

def solve():
    try:
        while True:
            N = int(input())
            O = [tuple(map(int, input().split())) for _ in range(N)]
            print(D(O))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
