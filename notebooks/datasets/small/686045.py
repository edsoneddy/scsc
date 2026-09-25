from queue import PriorityQueue


class Queue:
    def __init__(self, priority):
        self.priority = int(priority)

    def __lt__(self, other):
        return self.priority > other.priority


def main():
    enter = list(map(str, input().split()))
    pq = PriorityQueue()
    while True:
        if "T" in enter:
            break
        if "S" in enter:
            number = int(enter[1])
            pq.put(Queue(number))
        if "A" in enter:
            if not pq.empty():
                var = pq.get().priority
                print(var)
                pq.put(Queue(var))
            else:
                print("Error")
        if "R" in enter:
            if not pq.empty():
                pq.get()
            else:
                print("Error")
        if "I" in enter:
            if not pq.empty():
                number = int(enter[1])
                item = pq.get()
                var = item.priority + number
                pq.put(Queue(var))
            else:
                print("Error")
        if "D" in enter:
            if not pq.empty():
                number = int(enter[1])
                item = pq.get()
                var = item.priority - number
                pq.put(Queue(var))
            else:
                print("Error")
        enter = list(map(str, input().split()))


if __name__ == '__main__':
    main()
