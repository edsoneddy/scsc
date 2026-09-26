def identificar_estructura():
    import sys
    from collections import deque
    import heapq

    input = sys.stdin.read
    datos = input().splitlines()
    
    i = 0
    while i < len(datos):
        n = int(datos[i])
        i += 1

        stack = []
        queue = deque()
        p_queue = []
        
        es_stack = True
        es_queue = True
        es_priority_queue = True

        for _ in range(n):
            comando, x = map(int, datos[i].split())
            i += 1

            if comando == 1:  
                stack.append(x)
                queue.append(x)
                heapq.heappush(p_queue, -x) 
            elif comando == 2:  
                if es_stack:
                    if not stack or stack.pop() != x:
                        es_stack = False
                if es_queue:
                    if not queue or queue.popleft() != x:
                        es_queue = False
                if es_priority_queue:
                    if not p_queue or -heapq.heappop(p_queue) != x:
                        es_priority_queue = False

        posibles = sum([es_stack, es_queue, es_priority_queue])
        if posibles == 0:
            print("impossible")
        elif posibles > 1:
            print("not sure")
        elif es_stack:
            print("stack")
        elif es_queue:
            print("queue")
        elif es_priority_queue:
            print("priority queue")


if __name__ == "__main__":
    identificar_estructura()