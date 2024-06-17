import sys
from collections import defaultdict

n, m, v = map(int, sys.stdin.readline().split())

edges = []

for _ in range(m):
    edges.append(list(map(int, sys.stdin.readline().split())))

adj_list = defaultdict(list)

for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)

for a, b in edges:
    adj_list[a] = sorted(adj_list[a])
    adj_list[b] = sorted(adj_list[b])

def dfs(node, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, result)

visited = set()
result_dfs = []
dfs(v,visited, result_dfs)

def bfs(node, visited, result):
    for neighbor in adj_list.get(node, []):
        result.append(neighbor)
    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            bfs(neighbor, visited, result)
visited = set([v])
result_bfs = [v]
bfs(v,visited, result_bfs)

print(result_dfs)
print(result_bfs)





