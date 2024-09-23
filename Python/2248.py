import sys
input = lambda: sys.stdin.readline().rstrip()

N, L, I = map(int, input().split())
# dp[i][j] = i자리 이진수에서 1인 비트가 j개 존재할 때 개수
dp = [[0] * 32 for _ in range(32)]

# 초기값
for i in range(31):
    dp[0][i] = 1

for i in range(1, 32):
    # 이전 i자리값 불러오기
    dp[i][0] = dp[i-1][0]
    for j in range(1, 32):
        # i자리 2진수에서 1인 비트가 j개 존재할 때 점화식
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# 출력
for i in range(N, 0, -1):
    if I <= dp[i-1][L]:
        print(0, end='')
    else:
        print(1, end='')
        I -= dp[i-1][L]
        L -= 1
