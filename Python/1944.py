import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    def bfs(startR, startC):
        # 각자 위치까지의 최단거리 측정
        dq = deque([(startR, startC, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[startR][startC] = True
        while dq:
            r, c, d = dq.popleft()
            if maze[r][c] == 'S' or maze[r][c] == 'K':
                if startR != r or startC != c:
                    line.append((node[(startR, startC)], node[(r, c)], d))
            
            for mr, mc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r+mr, c+mc
                if maze[nr][nc] != '1' and not visited[nr][nc]:
                    dq.append((nr, nc, d+1))
                    visited[nr][nc] = True
    
    N, M = map(int, input().split())
    maze = []
    for _ in range(N):
        maze.append(list(input()))
    
    line = []
    node = dict()
    i = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 'S' or maze[r][c] == 'K':
                node[(r, c)] = i
                i += 1
    
    for r, c in node.keys():
        bfs(r, c)
    line.sort(key=lambda x: x[2])
    
    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if rank[r1] > rank[r2]:
            root[r2] = r1
        elif rank[r1] < rank[r2]:
            root[r1] = r2
        else:
            root[r2] = r1
            rank[r1] += 1
    def find(node):
        if root[node] != node:
            root[node] = find(root[node])
        return root[node]
    
    result = 0
    connected = 0
    root = [i for i in range(len(node))]
    rank = [0] * (len(node))
    for a, b, c in line:
        if find(a) != find(b):
            union(a, b)
            connected += 1
            result += c
            if connected == M:
                break
    print(result if connected == M else -1)

main()