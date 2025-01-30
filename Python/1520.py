import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(250000)

def main():
    def dfs(r, c):
        if dp[r][c] != -1:
            return dp[r][c]
        
        cases = 0
        for mr, mc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r+mr, c+mc
            if 0<=nr<M and 0<=nc<N and grid[r][c] < grid[nr][nc] and dp[nr][nc] != 0:
                cases += dfs(nr, nc)
        
        dp[r][c] = cases
        return cases
    
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    
    dp = [[-1] * N for _ in range(M)]
    dp[0][0] = 1
    dfs(M-1, N-1)
    print(dp[M-1][N-1])

main()