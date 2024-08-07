import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
state = list(map(int, list(input())))
targetState = list(map(int, list(input())))

# dp[i][j] = i번째 숫자판 j가 목표상태로 되는 최소 회전 수
dp = [[0]*10 for _ in range(N+1)]
path = [[0]*10 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(10):
        # 목표치와의 차이값
        diff = (targetState[i] - state[i] - j) % 10
        # 시계방향으로 회전
        l = dp[i+1][(diff+j) % 10] + diff
        # 반시계 방향 회전
        r = dp[i+1][j] + (10 - diff)

        if l < r:
            dp[i][j] = l
            path[i][j] = diff
        else:
            dp[i][j] = r
            path[i][j] = (diff - 10)

print(dp[0][0])

num = 0
for i in range(N):
    move = path[i][num]
    print(i+1, move)
    # 인덱스 오버 방지
    if move > 0:
        num = (num+move) % 10
