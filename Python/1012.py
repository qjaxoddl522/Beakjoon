import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

dx=[0,0,-1,1] #상하좌우
dy=[-1,1,0,0]
def worming(x, y):
    for i in range(4):
        if [x+dx[i], y+dy[i]] in cabbage:
            if [x+dx[i], y+dy[i]] not in cabbage_part:
                cabbage_part.append([x+dx[i], y+dy[i]])
                worming(x+dx[i], y+dy[i])

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    worm_num = 0
    cabbage = []
    for _ in range(K):
        cabbage.append(list(map(int, input().split())))

    while cabbage != []:
        cabbage_part = []
        x, y = cabbage[0][0], cabbage[0][1]
        
        cabbage_part.append([x, y])
        worming(x, y)
        
        cabbage = [x for x in cabbage if x not in cabbage_part]
        worm_num += 1
    print(worm_num)