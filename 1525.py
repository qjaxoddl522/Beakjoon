from collections import deque
import sys
input = sys.stdin.readline

mx = (1, -1, 0, 0)
my = (0, 0, 1, -1)
length = 3

def bfs():
    while q:
        qboard = q.popleft()

        if qboard == '123456780':
            return visited[qboard]
        
        z = qboard.index('0')
        x, y = z//length, z%length
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx<length and 0<=ny<length:
                nz = nx * length + ny
                boardList = list(qboard) #자리바꾸기용
                boardList[z], boardList[nz] = boardList[nz], boardList[z]
                nboard = ''.join(boardList)
                
                if nboard not in visited: #방문한적 없음
                    visited[nboard] = visited[qboard] + 1
                    q.append(nboard)
    return -1

board = ''
for _ in range(length):
    board += ''.join(input().rstrip().split())

q = deque()
q.append(board)
visited = {}
visited[board] = 0

print(bfs())
