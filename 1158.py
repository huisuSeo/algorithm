import sys

n, k = sys.stdin.readline().split()

n = int(n)
k = int(k)

s = []
p = []


for i in range(n):
    s.append(i + 1)
a = 0
while len(s) != 0:
    a += 1
    if a > len(s):
        a = a % k
    if a % k == 0:
        p.append(s[a - 1])
        s.remove(s[a - 1])

print(p)
