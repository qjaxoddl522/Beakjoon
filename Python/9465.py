""" 재귀 탑다운 방식
import sys

def stick(n, status): #0: 안뗌 1: 위쪽스티커 뗌 2: 아래쪽스티커 뗌
    if n == N:
        return 0
    if dp[n][status] != -1: #이미 저장된 답
        return dp[n][status]

    result = stick(n+1, 0) #안떼는 경우
    if status != 1: #왼쪽위의 스티커가 남아있을 경우
        result = max(result, stick(n+1, 1) + sticker[0][n])
    if status != 2: #왼쪽아래의 스티커가 남아있을 경우
        result = max(result, stick(n+1, 2) + sticker[1][n])

    dp[n][status] = result
    return result

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    dp = [[-1]*(3) for _ in range(N)]
    print(stick(0, 0))
"""
#반복문 바텀업 방식
import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    dp = [[0]*(3) for _ in range(N+1)]
    
    for i in range(N):
        dp[i+1][0] = max(dp[i+1][0], max(dp[i][0], max(dp[i][1], dp[i][2])))
        dp[i+1][1] = max(dp[i+1][1], max(dp[i][0], dp[i][2]) + sticker[0][i])
        dp[i+1][2] = max(dp[i+1][2], max(dp[i][0], dp[i][1]) + sticker[1][i])

    print(max(dp[N][0], max(dp[N][1], dp[N][2])))
