N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)] #N개 중에 K개 고르기

#기본 설정
for i in range(N+1):
    dp[i][0] = 1
for i in range(K+1):
    dp[i][i] = 1

#dp 바텀업
for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[N][K] % 10007)
