import sys
input = lambda: sys.stdin.readline().rstrip()

N, D = map(int, input().split())
shortcut = [list(map(int, input().split())) for _ in range(N)]

# dp[n] = n까지의 최소 거리
dp = [0 for _ in range(D+1)]

for i in range(1, D+1):
    nowMinDist = dp[i-1] + 1 # 현재 최소 거리
    for start, end, dist in shortcut:
        # 지름길 끝점이 현재 거리면 지름길 고려해보기
        if i == end:
            nowMinDist = min(nowMinDist, dp[start] +\
                             dist)
    dp[i] = nowMinDist
print(dp[D])
