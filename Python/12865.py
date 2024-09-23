import sys

N, K = map(int, input().split())
w, v = [0]*(N+1), [0]*(N+1) #무게, 가치
for i in range(1, N+1):
    w[i], v[i] = map(int, sys.stdin.readline().split())

#N번 까지 고려했을 때 가치합의 최댓값
dp = [[0] * (K+1) for _ in range(N+1)] #무게, 최댓값


for i in range(1, N+1):
    for j in range(1, K+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v[i] + dp[i-1][j-w[i]], dp[i-1][j])

print(dp[N][K])
