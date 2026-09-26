class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def to_list(head):
    out = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    return out

values = list(map(int, input().split()))
head = build_list(values)
reversed_head = reverse_list(head)
print(' '.join(to_list(reversed_head)))
