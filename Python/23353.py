import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    # [세로, 가로, 좌측대각선, 우측대각선] * 바꿔치기했을 경우
    dp = [[[[0, 0] for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                # 세로
                if r > 0:
                    dp[r][c][0][0] = dp[r-1][c][0][0] + 1
                    dp[r][c][0][1] = max(dp[r-1][c][0]) + 1
                else:
                    dp[r][c][0] = [1, 1]
                
                # 가로
                if c > 0:
                    dp[r][c][1][0] = dp[r][c-1][1][0] + 1
                    dp[r][c][1][1] = max(dp[r][c-1][1]) + 1
                else:
                    dp[r][c][1] = [1, 1]
                
                # 좌측대각선
                if r > 0 and c > 0:
                    dp[r][c][2][0] = dp[r-1][c-1][2][0] + 1
                    dp[r][c][2][1] = max(dp[r-1][c-1][2]) + 1
                else:
                    dp[r][c][2] = [1, 1]
                
                # 우측대각선
                if r > 0 and c < N-1:
                    dp[r][c][3][0] = dp[r-1][c+1][3][0] + 1
                    dp[r][c][3][1] = max(dp[r-1][c+1][3]) + 1
                else:
                    dp[r][c][3] = [1, 1]
            
            elif board[r][c] == 2:
                # 세로
                if r > 0:
                    dp[r][c][0][1] = dp[r-1][c][0][0] + 1
                else:
                    dp[r][c][0][1] = 1
                
                # 가로
                if c > 0:
                    dp[r][c][1][1] = dp[r][c-1][1][0] + 1
                else:
                    dp[r][c][1][1] = 1
                
                # 좌측대각선
                if r > 0 and c > 0:
                    dp[r][c][2][1] = dp[r-1][c-1][2][0] + 1
                else:
                    dp[r][c][2][1] = 1
                
                # 우측대각선
                if r > 0 and c < N-1:
                    dp[r][c][3][1] = dp[r-1][c+1][3][0] + 1
                else:
                    dp[r][c][3][1] = 1
            
            else:
                dp[r][c] = [[0, 0] for _ in range(4)]
            answer = max(answer, max(dp[r][c][0]), max(dp[r][c][1]), max(dp[r][c][2]), max(dp[r][c][3]))
    print(answer)

main()