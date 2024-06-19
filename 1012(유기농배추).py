import sys

input = sys.stdin.readline

T = int(input())

M = []
N = []
K = []

graph = []
result = []
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



for _ in range(T):
    TM, TN, TK = input().split()
    TM = int(TM)
    TN = int(TN)
    TK = int(TK)

    M.append(TM)
    N.append(TN)
    K.append(TK)

    for _ in range(TK):
        graph.append(list(map(int, input().rstrip().split())))




def dfs(x, y, m, n, l):
    global count

    if x < 0 or x >= m or y < 0 or y >= n:
        return

    if graph[l] == [x,y]:
        count += 1
        graph[l] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, m, n, l)


for i in (T):
    for j in range(M[i]):
        for k in range(N[i]):
            for l in range(K[i]):
                if graph[l] == [j,k]:
                    dfs(j, k, M[i], N[i], l)
                    result.append(count)
                    count = 0

print(*result)


