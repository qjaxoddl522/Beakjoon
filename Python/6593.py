from collections import deque
import sys
input = sys.stdin.readline

while True:
    L, R, C = map(int, input().rstrip().split())
    if L == 0 and R == 0 and C == 0: #끝내기
        break

    S = [0, 0, 0] #시작지점 [층, 행, 열]
    E = [0, 0, 0] #출구지점
    
    maze = []
    for i in range(L):
        maze.append([])
        for j in range(R):
            m = list(input().rstrip())
            if 'S' in m: #시작지점 찾기
                S = [i, j, m.index('S')]
            if 'E' in m: #출구지점 찾기
                E = [i, j, m.index('E')]
            maze[i].append(m)
        input()

    result = [[[0] * C for _ in range(R)] for _ in range(L)] #S로부터 걸린 이동시간
    
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[S[0]][S[1]][S[2]] = True
    q = deque([S])
    
    mf = [1, -1, 0, 0, 0, 0]
    mx = [0, 0, 1, -1, 0, 0]
    my = [0, 0, 0, 0, 1, -1]

    while q:
        loc = q.popleft() #현재 위치
        for i in range(6):
            f = loc[0]+mf[i]
            x = loc[1]+mx[i]
            y = loc[2]+my[i]
            if f>=0 and f<L and x>=0 and x<R and y>=0 and y<C: #범위 안이고
                if (maze[f][x][y] == '.' or maze[f][x][y] == 'E') and not visited[f][x][y]: #이동가능한 방문한적 없는 장소면
                    q.append([f, x, y]) #큐에 추가하고 방문처리
                    result[f][x][y] = result[loc[0]][loc[1]][loc[2]] + 1
                    visited[f][x][y] = True

    ans = result[E[0]][E[1]][E[2]] #정답 출력
    print("Escaped in {0} minute(s).".format(ans) if ans > 0 else "Trapped!")
