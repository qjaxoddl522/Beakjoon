import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(n)]

ans = 0
# dp[i][j] = 연속된 정사각형의 길이
dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            # 이전 좌표들도 정사각형을 형성
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans**2)