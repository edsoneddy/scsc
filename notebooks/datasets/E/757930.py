from collections import deque
import heapq

def f(ops):
    s, q, p = [], deque(), []
    cs, cq, cp = True, True, True

    for op, x in ops:
        if op == 1:
            s.append(x)
            q.append(x)
            heapq.heappush(p, -x)
        elif op == 2:
            if s and s[-1] == x:
                s.pop()
            else:
                cs = False
            if q and q[0] == x:
                q.popleft()
            else:
                cq = False
            if p and -p[0] == x:
                heapq.heappop(p)
            else:
                cp = False

    cnt = sum([cs, cq, cp])

    if cnt == 0:
        return "impossible"
    elif cnt > 1:
        return "not sure"
    else:
        if cs:
            return "stack"
        if cq:
            return "queue"
        if cp:
            return "priority queue"

def main():
    try:
        while True:
            n = int(input())
            ops = [tuple(map(int, input().split())) for _ in range(n)]
            print(f(ops))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
