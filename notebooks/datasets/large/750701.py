from queue import PriorityQueue
from queue import Queue
import sys
while True:
    
    linea = sys.stdin.readline()
    
    if not linea:
        break
    num = int(linea.strip())
    
    instructions = []
    elements = []
    
    for _ in range(num):
        instruction, element = map(int, sys.stdin.readline().strip().split())
        instructions.append(instruction)
        elements.append(element)

    queue = Queue()
    priority_queue = PriorityQueue()
    stack = []

    is_queue = True
    is_priority_queue = True
    is_stack = True

    for instruction, element in zip(instructions, elements):
        if instruction == 1:
            queue.put(element)
            priority_queue.put((-element, -element))
            stack.append(element)
        elif instruction == 2:
            if not queue.empty() and is_queue:
                top_element = queue.get()
                # print(queue.queue)
                if top_element != element:
                    is_queue = False
            else:
                is_queue = False
            if not priority_queue.empty() and is_priority_queue:
                top_element = - priority_queue.get()[0]
                # print(priority_queue.queue)
                # print(f'top {top_element} and element {element}')
                if top_element != element:
                    is_priority_queue = False
            else:
                is_priority_queue = False
            if stack:
                top_element = stack.pop()
                # print(stack)
                if top_element!= element:
                    is_stack = False
            else:
                is_stack = False

    # Case
    if is_queue or is_priority_queue or is_stack:
        # print(is_queue + is_priority_queue + is_stack)
        if (is_queue + is_priority_queue + is_stack) == 1:
            if is_queue:
                print('queue')
            elif is_priority_queue:
                print('priority queue')
            elif is_stack:
                print('stack')
        else:
            print('not sure')
    else:
        print("impossible")