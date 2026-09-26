import sys
from collections import deque
from heapq import *

for k in sys.stdin:
    if k.strip() != "":
        N = int(k.strip())
        stack = []
        queue = deque()
        heap = []
        isStack = isQueue = isHeap = 1
        for i in range(N):
            x, y = map(int, input().split())
            if x == 1:
                stack.append(y)
                queue.append(y)
                heappush(heap, -y)
            else:
                a = stack.pop() if stack else None
                if a != y:
                    isStack = 0
                a = queue.popleft() if queue else None
                if a != y:
                    isQueue = 0
                a = -heappop(heap) if heap else None
                if a != y:
                    isHeap = 0
        s = sum([isStack, isQueue, isHeap])
        if s >= 2:
            print('not sure')
        elif s == 0:
            print('impossible')
        else:
            if isStack:
                print('stack')
            if isQueue:
                print('queue')
            if isHeap:
                print('priority queue')

# O(nlogn)