N = int(input())
video = [list(map(int, input())) for _ in range(N)]

def loop(x, y, n): #첫 x좌표, 첫 y좌표, 간격
    check = video[x][y] #영상이 동일한지 확인용
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != video[i][j]: #같지 않은 영상이 있으면 루프
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        loop(x, y, n) #4분할 루프
        loop(x, y+n, n)
        loop(x+n, y, n)
        loop(x+n, y+n, n)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')
loop(0, 0, N)
