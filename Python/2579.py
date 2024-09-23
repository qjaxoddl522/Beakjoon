import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * (301)
for i in range(1, n+1):
    stair[i] = int(input())
dp = [0] * (301) #n번째 계단 까지의 최대 점수
dp[1], dp[2], dp[3] = stair[1], stair[1] + stair[2], max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n+1):
    #(i-1번째 계단에서 오는 경우) vs (i-2번째 계단에서 오는 경우)
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n])
