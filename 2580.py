import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

def row(x, n): #x인덱스, 넣을 숫자
    for i in range(9):
        if board[x][i] == n: #겹치는 숫자 발견
            return False
    return True

def col(y, n): #x인덱스, 넣을 숫자
    for i in range(9):
        if board[i][y] == n: #겹치는 숫자 발견
            return False
    return True

def square(x, y, n): #x인덱스, y인덱스, 넣을 숫자
    nx, ny = x//3*3, y//3*3 #박스 위치
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] == n: #겹치는 숫자 발견
                return False
    return True

def backtrack(idx): #조사중인 y 인덱스
    if idx == len(blank): #빈칸 전부 채움
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if row(x, i) and col(y, i) and square(x, y, i):
            board[x][y] = i
            backtrack(idx+1)
            board[x][y] = 0 #되돌려놓기

board = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i,j])
backtrack(0)
