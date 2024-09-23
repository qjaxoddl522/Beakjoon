import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
need = [int(input()) for _ in range(n)]

result = []
stack = deque()
for i in range(1, n+1):
    stack.append(i)
    result.append('+')

    while need and stack and need[0] == stack[-1]:
        stack.pop()
        need.pop(0)
        result.append('-')

if stack:
    print("NO")
else:
    print('\n'.join(result))
