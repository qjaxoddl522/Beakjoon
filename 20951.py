import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 10 ** 9 + 7

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# dp[i][j] = i번 이동하여 j번 정점에 도착했을 때 가지는 경우의 수
dp = [[0] * (N+1) for _ in range(8)]
dp[0] = [1] * (N+1)
for i in range(1, 8):
    for j in range(1, N+1):
        for node in tree[j]:
            dp[i][j] = (dp[i][j] + dp[i-1][node]) % MOD
print(sum(dp[7]) % MOD)