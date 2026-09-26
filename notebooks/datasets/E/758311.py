from collections import deque
import heapq

def guess_structure():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        stack = []
        queue = deque()
        pq = []
        is_stack = is_queue = is_pq = True

        for _ in range(n):
            op, x = map(int, input().split())

            if op == 1:
                stack.append(x)
                queue.append(x)
                heapq.heappush(pq, -x)  # Use negative for max heap
            else:
                if not stack or stack.pop() != x:
                    is_stack = False
                if not queue or queue.popleft() != x:
                    is_queue = False
                if not pq or -heapq.heappop(pq) != x:
                    is_pq = False

        possible_structures = sum([is_stack, is_queue, is_pq])

        if possible_structures == 0:
            print("impossible")
        elif possible_structures > 1:
            print("not sure")
        elif is_stack:
            print("stack")
        elif is_queue:
            print("queue")
        elif is_pq:
            print("priority queue")

# Run the function
guess_structure()