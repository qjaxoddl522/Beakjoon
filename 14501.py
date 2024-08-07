import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 상담 기간, 이익
priceDay = [0] * (N+1)
benefit = [0] * (N+1)
for i in range(1, N+1):
    priceDay[i], benefit[i] = map(int, input().split())

# dp[i] = i일차에서 최대 이익
dp = [0] * (N+2)
for i in range(1, N+1):
    # 설정된 이익과 전날 이익 dp 갱신
    dp[i] = max(dp[i-1], dp[i])
    # 가능한 상담 진행 후 dp 갱신
    end = i+priceDay[i]
    if end <= N+1:
        dp[end] = max(dp[i] + benefit[i], \
                      dp[i+priceDay[i]])
dp[N+1] = max(dp[N], dp[N+1])

print(dp[N+1])
