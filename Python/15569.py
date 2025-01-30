import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1999

def main():
    N, M = map(int, input().split())
    # dp[i][j] = i*j 크기의 블럭을 만드는 경우의 수
    dp = [[0]*(N+1) for _ in range(max(N, M)+1)]
    dp[N][0], dp[N][1], dp[1][N] = 1, 1, 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            dp[N][i] += dp[N][i-j]
        dp[N][i] %= MOD
        dp[i][N] = dp[N][i]
    
    NN = dp[N][N] - 1
    dp[N][N] = ((dp[N][N] * 2) - 1) % MOD
    for i in range(N+1, M+1):
        for j in range(1, N+1):
            if j == N:
                dp[i][N] += dp[i-j][N] * (1 + NN)
            else:
                dp[i][N] += dp[i-j][N]
        dp[i][N] %= MOD
    print(dp[M][N])

main()