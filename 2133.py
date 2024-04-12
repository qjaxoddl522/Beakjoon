import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (31) #N이 홀수일 경우는 무조건 0
dp[1], dp[2] = 0, 3

for i in range(4, N+1):
    if i%2 == 1:
        continue
    dp[i] = dp[i-2]*3
    for j in range(0, i-2, 2):
        dp[i] += dp[j]*2
    dp[i] += 2

print(dp[N])
