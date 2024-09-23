import sys
input = sys.stdin.readline

dp = [0] * 11 #최대 10
dp[1], dp[2], dp[3] = 1, 2, 4

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        if dp[i] == 0: #i가 4이상일 경우 점화식
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
