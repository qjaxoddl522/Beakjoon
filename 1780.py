N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

resMinus = 0
resZero = 0
resPlus = 0

def loop(x, y, n):
    global resMinus, resZero, resPlus #변수 불러오기

    check = paper[x][y] #같은지 확인하기 위한 변수
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != check: #같지 않은 종이가 있으면 재귀
                for k in range(3):
                    for l in range(3):
                        loop(x+(k*n//3), y+(l*n)//3, n//3) #시작점, 길이 재지정
                return

    if check == -1:
        resMinus += 1
    elif check == 0:
        resZero += 1
    else:
        resPlus += 1

loop(0, 0, N) #시작x, 시작y, 길이
print(resMinus, resZero, resPlus, sep="\n")
