import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    M, N = map(int, input().split())
    grid = [list(input().split()) for _ in range(M)]
    
    dp = [[0]*N for _ in range(M)]
    answer = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "0":
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                answer = max(answer, dp[i][j])
    print(answer)

main()