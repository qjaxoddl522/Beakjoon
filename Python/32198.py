import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = float('inf')

N = int(input())
bang = [list(map(int, input().split())) for _ in range(N)]
bang.sort(key=lambda x: x[0])
lastBang = bang[-1][0]

# dp[i][j] = i초 후 위치 j까지 이동 거리
dp = [[MAX] * 2001 for _ in range(lastBang+1)]
dp[0][1000] = 0

time, left, right = bang.pop(0)
for i in range(1, lastBang+1):
    for j in range(1000-i, 1000+i+1):
        dp[i][j] = min(\
        dp[i-1][max(0, j-1)]+1,
        dp[i-1][j],
        dp[i-1][min(2000, j+1)]+1, MAX)
    if time == i:
        dp[i][1000+left+1:1000+right] = [MAX] * (right-left-1)
        if bang:
            time, left, right = bang.pop(0)
result = min(dp[-1])
print(result if result != MAX else -1)