import sys
from collections import deque
from heapq import heappush, heappop

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            N = int(line)
            stack = []
            queue = deque()
            heap = []
            is_stack = True
            is_queue = True
            is_heap = True

            for _ in range(N):
                command, value = map(int, input().split())
                if command == 1:
                    stack.append(value)
                    queue.append(value)
                    heappush(heap, -value)
                elif command == 2:
                    if stack:
                        stack_value = stack.pop()
                    else:
                        stack_value = None
                    if queue:
                        queue_value = queue.popleft()
                    else:
                        queue_value = None
                    if heap:
                        heap_value = -heappop(heap)
                    else:
                        heap_value = None

                    if stack_value != value:
                        is_stack = False
                    if queue_value != value:
                        is_queue = False
                    if heap_value != value:
                        is_heap = False

            results = sum([is_stack, is_queue, is_heap])
            if results >= 2:
                print('not sure')
            elif results == 0:
                print('impossible')
            else:
                if is_stack:
                    print('stack')
                if is_queue:
                    print('queue')
                if is_heap:
                    print('priority queue')

if __name__ == "__main__":
    main()
