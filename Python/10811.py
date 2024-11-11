import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ls = list(range(1, N+1))
for _ in range(M):
    s, e = map(int, input().split())
    ls[s-1:e] = ls[::-1][N-e:N-s+1]
print(*ls)