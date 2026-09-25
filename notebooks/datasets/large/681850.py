import sys
from collections import deque
from heapq import heappush, heappop
def identificar(op):
    s = []
    q = deque()
    h = []
    isS = True
    isQ = True
    isH = True
    for op in op:
        c, v = op
        if c == 1:
            s.append(v)
            q.append(v)
            heappush(h, -v)
        elif c == 2:
            if s:
                sv = s.pop()
            else:
                isS = False
            if q:
                qv = q.popleft()
            else:
                isQ = False
            if h:
                hv = -heappop(h)
            else:
                isH = False
            if isS and sv != v:
                isS = False
            if isQ and qv != v:
                isQ = False
            if isH and hv != v:
                isH = False
    ps = sum([isS, isQ, isH])
    if ps == 0:
        return 'impossible'
    elif ps > 1:
        return 'not sure'
    else:
        if isS:
            return 'stack'
        elif isQ:
            return 'queue'
        elif isH:
            return 'priority queue'
def main():
    inp = sys.stdin.read
    dat = inp().strip().split('\n')
    ind = 0
    res = []
    while ind < len(dat):
        n = int(dat[ind].strip())
        ind += 1
        op = []
        for i in range(n):
            com, v = map(int, dat[ind].strip().split())
            op.append((com, v))
            ind += 1
        r = identificar(op)
        res.append(r)
    for r in res:
        print(r)
if __name__ == "__main__":
    main()