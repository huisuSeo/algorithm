import sys
from collections import defaultdict, deque

n, m, v = map(int, sys.stdin.readline().split())

edges = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))
    edges.append((b, a))  # 양방향 간선 처리

adj_list = defaultdict(list)

for a, b in edges:
    adj_list[a].append(b)

for key in adj_list.keys():
    adj_list[key].sort()


def dfs(node, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, result)

visited = set()
result_dfs = []
dfs(v,visited, result_dfs)

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result_bfs = [start]

    while queue:
        node = queue.popleft()
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                result_bfs.append(neighbor)
    return result_bfs

result_bfs = bfs(v)


print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))





