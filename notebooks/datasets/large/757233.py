from collections import deque
import sys

int_to_check = 0
stack_test_list = []
queue_test_list = deque([])
priority_test_list = []
is_boolean_possible = could_be_stack = could_be_queue = could_be_priority = True

for line in sys.stdin:
    if " " not in line:
        int_to_check = int(line)
    else:
        value_string = line.split(" ")
        integer_value = int(value_string[1])
        if value_string[0] == "1":
            stack_test_list.append(integer_value)
            queue_test_list.append(integer_value)
            priority_test_list.append(integer_value)
            int_to_check -= 1
        else:
            if not any([integer_value in stack_test_list, integer_value in queue_test_list, integer_value in
                        priority_test_list]):
                is_boolean_possible = False
            else:
                if could_be_priority:
                    if max(priority_test_list) != integer_value:
                        could_be_priority = False
                    if integer_value in priority_test_list:
                        priority_test_list.remove(integer_value)
                if could_be_queue:
                    if queue_test_list.popleft() != integer_value:
                        could_be_queue = False
                if could_be_stack:
                    if stack_test_list.pop() != integer_value:
                        could_be_stack = False
            int_to_check -= 1
    if int_to_check == 0:
        if not is_boolean_possible or sum([could_be_stack, could_be_queue, could_be_priority]) == 0:
            print("impossible")
        elif sum([could_be_stack, could_be_queue, could_be_priority]) > 1:
            print("not sure")
        elif could_be_stack:
            print("stack")
        elif could_be_queue:
            print("queue")
        else:
            print("priority queue")

        stack_test_list = []
        queue_test_list = deque([])
        priority_test_list = []
        is_boolean_possible = could_be_stack = could_be_queue = could_be_priority = True