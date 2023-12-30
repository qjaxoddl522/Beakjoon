def check(b):
    res = 0
    for i in range(n):
        cnt = 1
        for j in range(n-1): #행 검사
            if b[i][j] == b[i][j+1]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(n-1): #열 검사
            if b[j][i] == b[j+1][i]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
    return res

n = int(input())
board = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if j+1 < n: #행이 끝부분인지 확인
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            result = max(result, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] #계산 후 원래대로
        if i+1 < n: #열이 끝부분인지 확인
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            result = max(result, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] #계산 후 원래대로

print(result)
