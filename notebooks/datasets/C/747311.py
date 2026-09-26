import sys
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.numElements = 0

    def isEmpty(self):
        return self.numElements == 0

    def insert(self, data):
        heapq.heappush(self.queue, -data)
        self.numElements += 1

    def get_max(self):
        if not self.isEmpty():
            return -self.queue[0]
        else:
            return None

    def extract_max(self):
        if not self.isEmpty():
            self.numElements -= 1
            return -heapq.heappop(self.queue)
        else:
            return None

    def change_max_priority(self, data):
        if not self.isEmpty():
            heapq.heappop(self.queue)
            heapq.heappush(self.queue, -data)

# Procesar las entradas
queue = PriorityQueue()
OUTPUT = ''
while True:
    linea = sys.stdin.readline().strip()
    if not linea:
        break
    linea_elements = list(linea.split())
    if len(linea_elements) > 1:
        instruction = linea_elements[0]
        num = int(linea_elements[1])
        if instruction == 'S':
            queue.insert(num)
        elif instruction == 'I':
            maxElement = queue.get_max()
            if maxElement is not None:
                queue.change_max_priority(maxElement + num)
            else:
                OUTPUT += 'Error' +'\n'    
        elif instruction == 'D':
            maxElement = queue.get_max()
            if maxElement is not None:
                queue.change_max_priority(maxElement - num)
            else:
                OUTPUT += 'Error' +'\n'    
    else:
        instruction = linea_elements[0]
        if instruction == 'A':
            maxElement = queue.get_max()
            if maxElement is not None:
                OUTPUT += str(maxElement) +'\n'
            else:
                OUTPUT += 'Error' +'\n'      
        elif instruction == 'R':
            maxElement = queue.extract_max()
            if maxElement is None:
                OUTPUT += 'Error' +'\n'
        elif instruction == 'T':
            break

print(OUTPUT, end = '')

