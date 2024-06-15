import sys

k, n = map(int, sys.stdin.readline().split())

lines = []

for _ in range(k):
    lines.append(int(sys.stdin.readline()))

start, end = 1, max(lines)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for line in lines:
        if line >= mid:
            sum += round(line // mid)

    if sum < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
