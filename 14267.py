import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
boss = list(map(int, input().split()))

# 받은 칭찬
comp = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    comp[i] += w

# 미리 모든 칭찬을 받아놓고 부하에게 같은 양의 칭찬을 전달한다
for i in range(2, n+1):
    comp[i] += comp[boss[i-1]]

print(*comp[1:])
