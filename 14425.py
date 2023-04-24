import sys

n, m = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline() for _ in range(n))

num = 0
for _ in range(m):
    if sys.stdin.readline() in s:
        num += 1

print(num)
