import heapq

def identificar_estructura(n, v):
    s = []
    q = []
    pq = []
    es_s = True
    es_q = True
    es_pq = True

    for op in v:
        t, x = op
        if t == 1:
            s.append(x)
            q.append(x)
            heapq.heappush(pq, -x)
        elif t == 2:
            if es_s:
                if not s or s.pop() != x:
                    es_s = False
            if es_q:
                if not q or q.pop(0) != x:
                    es_q = False
            if es_pq:
                if not pq or -heapq.heappop(pq) != x:
                    es_pq = False

    if es_s and not es_q and not es_pq:
        return "stack"
    elif not es_s and es_q and not es_pq:
        return "queue"
    elif not es_s and not es_q and es_pq:
        return "priority queue"
    elif not es_s and not es_q and not es_pq:
        return "impossible"
    else:
        return "not sure"

while True:
    try:
        n = int(input().strip())
        v = []
        for _ in range(n):
            t, x = map(int, input().strip().split())
            v.append((t, x))
        print(identificar_estructura(n, v))
    except EOFError:
        break

