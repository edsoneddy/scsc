import heapq
op = []
while True:
    com = input().split()
    if com[0] == "S":
        heapq.heappush(op, -int(com[1]))
    elif com[0] == "A":
        if op:
            print(-op[0])
        else:
            print("Error")
    elif com[0] == "R":
        if op:
            heapq.heappop(op)
        else:
            print("Error")
    elif com[0] == "I":
        if op:
            op[0] -= int(com[1])
            heapq.heapify(op)
        else:
            print("Error")
    elif com[0] == "D":
        if op:
            op[0] += int(com[1])
            heapq.heapify(op)
        else:
            print("Error")
    elif com[0] == "T":
        break
