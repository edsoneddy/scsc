import heapq

operations = []
while True:
    command = input().split()
    if command[0] == "S":
        heapq.heappush(operations, -int(command[1]))
    elif command[0] == "A":
        if operations:
            print(-operations[0])
        else:
            print("Error")
    elif command[0] == "R":
        if operations:
            heapq.heappop(operations)
        else:
            print("Error")
    elif command[0] == "I":
        if operations:
            operations[0] -= int(command[1])
            heapq.heapify(operations)
        else:
            print("Error")
    elif command[0] == "D":
        if operations:
            operations[0] += int(command[1])
            heapq.heapify(operations)
        else:
            print("Error")
    elif command[0] == "T":
        break
