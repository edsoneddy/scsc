import sys
from collections import deque
import heapq

def identify_structure(commands):
    stack, queue, pqueue = [], deque(), []
    possible_stack, possible_queue, possible_pqueue = True, True, True

    for cmd, x in commands:
        if cmd == 1:
            if possible_stack:
                stack.append(x)
            if possible_queue:
                queue.append(x)
            if possible_pqueue:
                heapq.heappush(pqueue, -x)
        elif cmd == 2:
            if possible_stack:
                if not stack or stack.pop() != x:
                    possible_stack = False
            if possible_queue:
                if not queue or queue.popleft() != x:
                    possible_queue = False
            if possible_pqueue:
                if not pqueue or -heapq.heappop(pqueue) != x:
                    possible_pqueue = False

    count = sum([possible_stack, possible_queue, possible_pqueue])
    if count == 0:
        return "impossible"
    elif count > 1:
        return "not sure"
    else:
        if possible_stack:
            return "stack"
        if possible_queue:
            return "queue"
        if possible_pqueue:
            return "priority queue"

def main():
    input = sys.stdin.read().strip().split("\n")
    i = 0
    results = []
    while i < len(input):
        n = int(input[i])
        i += 1
        commands = [tuple(map(int, input[j].split())) for j in range(i, i + n)]
        i += n
        results.append(identify_structure(commands))
    print("\n".join(results))

if __name__ == "__main__":
    main()
