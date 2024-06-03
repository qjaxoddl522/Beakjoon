import sys
input = sys.stdin.readline

def divide(x, y, l):
    #기준 색(하나라도 다르면 분할)
    standardColor = board[x][y]
    for i in range(x, x+l):
        for j in range(y, y+l):
            if board[i][j] != standardColor:
                divide(x, y, l//2)
                divide(x+l//2, y, l//2)
                divide(x, y+l//2, l//2)
                divide(x+l//2, y+l//2, l//2)
                return
    #모두 같으면 해당 색+1
    paperNum[standardColor] += 1

N = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

#각 색종이의 개수 [하얀색, 파란색]
paperNum = [0, 0]
divide(0, 0, N)
print(*paperNum, sep='\n')
