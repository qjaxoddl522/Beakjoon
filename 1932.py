import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n+1)] #dp[x][y] = x번째 줄 y번째의 최대합
dp[0][0] = arr[0][0]

for x in range(1, n):
    dp[x][0] = dp[x-1][0] + arr[x][0]
    for y in range(1, x):
        dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + arr[x][y]
    dp[x][x] = dp[x-1][x-1] + arr[x][x]

print(max(dp[n-1]))
