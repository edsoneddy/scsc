import heapq
def main():
    while True:
        try:
            n = int(input())
            commands = [input().split() for _ in range(n)]
            is_stack = is_queue = is_priority_queue = True
            stack = []
            queue = []
            priority_queue = []
            for cmd in commands:
                operation, value = int(cmd[0]), int(cmd[1])
                if operation == 1:
                    stack.append(value)
                    queue.append(value)
                    heapq.heappush(priority_queue, -value)
                else:
                    if len(stack) == 0 or stack.pop() != value:
                        is_stack = False
                    if len(queue) == 0 or queue.pop(0) != value:
                        is_queue = False
                    if len(priority_queue) == 0 or -heapq.heappop(priority_queue) != value:
                        is_priority_queue = False
            if is_stack and not is_queue and not is_priority_queue:
                print("stack")
            elif not is_stack and is_queue and not is_priority_queue:
                print("queue")
            elif not is_stack and not is_queue and is_priority_queue:
                print("priority queue")
            elif not is_stack and not is_queue and not is_priority_queue:
                print("impossible")
            else:
                print("not sure")
        except EOFError:
            break
if __name__ == "__main__":
    main()