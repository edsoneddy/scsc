from queue import PriorityQueue

while True:
    try:
        n = int(input())
        stack_ok = True
        queue_ok = True
        priority_queue_ok = True
        stack = []
        queue = []
        priority_queue = PriorityQueue()

        for _ in range(n):
            op, x = map(int, input().split())
            if op == 1:
                stack.append(x)
                queue.append(x)
                priority_queue.put(-x)
            else:
                if not stack or stack.pop() != x:
                    stack_ok = False
                if not queue or queue.pop(0) != x:
                    queue_ok = False
                if priority_queue.empty() or -priority_queue.get() != x:
                    priority_queue_ok = False

        if stack_ok + queue_ok + priority_queue_ok == 0:
            print("impossible")
        elif stack_ok + queue_ok + priority_queue_ok > 1:
            print("not sure")
        elif stack_ok:
            print("stack")
        elif queue_ok:
            print("queue")
        else:
            print("priority queue")

    except EOFError:
        break
