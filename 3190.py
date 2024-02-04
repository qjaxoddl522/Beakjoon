import sys
input = sys.stdin.readline

second = 0

N = int(input())
board = [[0] * N for _ in range(N)]
snake, dire = [], 1 #0위 1오른쪽 2아래쪽 3왼쪽

apple = [list(map(int, input().split())) for _ in range(int(input()))]
#사과를 2로 지정
for a in apple:
    board[a[0]-1][a[1]-1] = 2
#뱀은 1로 지정
snake.append([0, 0])
board[0][0] = 1

move = [input().split() for _ in range(int(input()))]

while(True):
    second += 1
    if dire == 0:
        if snake[-1][0] > 0:
            snake.append([snake[-1][0] - 1, snake[-1][1]])
        else: #벽 충돌
            break
    elif dire == 1:
        if snake[-1][1] < N - 1:
            snake.append([snake[-1][0], snake[-1][1] + 1])
        else: #벽 충돌
            break
    elif dire == 2:
        if snake[-1][0] < N - 1:
            snake.append([snake[-1][0] + 1, snake[-1][1]])
        else: #벽 충돌
            break
    elif dire == 3:
        if snake[-1][1] > 0:
            snake.append([snake[-1][0], snake[-1][1] - 1])
        else: #벽 충돌
            break
    
    if board[snake[-1][0]][snake[-1][1]] == 1: #몸통 충돌
        break
    if board[snake[-1][0]][snake[-1][1]] != 2: #사과가 있으면 꼬리 생략
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0
    board[snake[-1][0]][snake[-1][1]] = 1 #머리 갱신

    #방향전환
    if move and int(move[0][0]) == second:
        if move[0][1] == 'L':
            dire = (dire - 1) % 4
        elif move[0][1] == 'D':
            dire = (dire + 1) % 4
        move.pop(0)
print(second)
