import sys
from collections import deque

input = sys.stdin.readline

N, K = input().split()

visited = []


def bfs(N, count):
    count = 0
    while K in visited:
        if N - 1 >= 0:
            visited.append(N - 1)
            visited.append(N + 1)
            visited.append(N * 2)
        else:
            visited.append(N + 1)
            visited.append(N * 1)
        if K in visited:
            break
        else:
            visited.pop(N)


        for i in visited:
            bfs(visited[i], count)
        count = count + 1

    return count

print(bfs(int(N), 0))
