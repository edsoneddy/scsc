from collections import deque

def bfs_distance(graph, start, end):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
start, end = map(int, input().split())
print(bfs_distance(graph, start, end))
