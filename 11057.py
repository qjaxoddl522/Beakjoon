N = int(input())
dp = [[0] * (10) for _ in range(N+1)] #dp[i][j] = 길이가 i이고 마지막 숫자가 j인 오르막수
for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1): #길이
    for j in range(10): #마지막 숫자
        dp[i][j] = sum([dp[i-1][k] for k in range(j, 10)])

print(sum(dp[N]) % 10007)
