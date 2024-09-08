import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    # 주변 4방향과 겹치지 않는지 확인
    def isValid(selected, r, c):
        for i in selected:
            _, otherR, otherC = grid[i]
            if abs(r-otherR) + abs(c-otherC) <= 1:
                return False
        return True

    def backtrack(selected, start, end, value, maxValue):
        if len(selected) == K:
            return max(value, maxValue)
        
        for i in range(start, end+1):
            if isValid(selected, grid[i][1], grid[i][2]):
                selected.append(i)
                maxValue = backtrack(selected, i+1, end, value + grid[i][0], maxValue)
                selected.pop()
        return max(value, maxValue)
    
    N, M, K = map(int, input().split())
    grid = []
    for i in range(N):
        for j, value in enumerate(list(map(int, input().split()))):
            grid.append((value, i, j))
    grid.sort(reverse=True, key=lambda x: x[0])
    return backtrack([], 0, min(N*M-1, K**2), 0, 0)

print(solve())