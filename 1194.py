import sys
input = sys.stdin.readline
from collections import deque

mx = (1, -1, 0, 0)
my = (0, 0, 1, -1)

N, M = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]

#현재 문에 맞는 키가 있는지 확인
def keyCheck(key_bit, door): #(키 비트, 문 위치)
    a = key_bit & (1 << (ord(door) - ord('A')))
    return True if a else False

def bfs(x, y):
    q = deque([(x, y, 0, 0)]) #[x, y, 이동 횟수, 가지고 있는 키 비트]
    #visited[x][y][가지고 있는 키 비트]
    visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = True #시작점 방문처리

    while q:
        x, y, move, key = q.popleft()

        #도착지점이면 최솟값 리턴
        if board[x][y] == '1':
            return move

        for i in range(4):
            nx = x+mx[i]
            ny = y+my[i]
            if 0 <= nx < N and 0 <= ny < M:
                #현재 키 상태에서 방문한 적 없음
                if not visited[nx][ny][key]:
                    if board[nx][ny] == '1' or board[nx][ny] == '.':
                        #갈 수 있는 공간이면 큐에 삽입
                        visited[nx][ny][key] = True
                        q.append((nx, ny, move+1, key))
                    elif 'a' <= board[nx][ny] <= 'f':
                        #열쇠면 먹고 큐에 삽입
                        key_new = key | (1 << (ord(board[nx][ny]) - ord('a')))
                        visited[nx][ny][key_new] = True
                        q.append((nx, ny, move+1, key_new))
                    elif 'A' <= board[nx][ny] <= 'F':
                        #잠긴 문이면 키 있는지 확인 후 큐에 삽입
                        if keyCheck(key, board[nx][ny]):
                            visited[nx][ny][key] = True
                            q.append((nx, ny, move+1, key))
    #큐 탐색 종료 후 출구를 찾지 못하면 -1 리턴
    return -1

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            board[i][j] = '.'
            print(bfs(i, j))
