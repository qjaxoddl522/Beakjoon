import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
basket = [0 for _ in range(N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for num in range(i, j+1):
        basket[num] = k

print(*basket[1:])
