import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N = int(input())
    sx, sy = map(int, input().split())
    moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
    
    def valid(x, y):
        return 1 <= x <= N and 1 <= y <= N
    
    def calculate(x, y):
        neighbors = []
        for dx1, dy1 in moves:
            nx, ny = x + dx1, y + dy1
            if valid(nx, ny):
                for dx2, dy2 in moves:
                    rx, ry = nx + dx2, ny + dy2
                    if valid(rx, ry):
                        neighbors.append((rx, ry))
        return neighbors

    if N >= 7:
        if (sx + sy) % 2 == 0:
            ans = ((N + 1) // 2) ** 2 + (N // 2) ** 2
        else:
            ans = 2 * ((N + 1) // 2) * (N // 2)
        print(ans)
        return

    visited = set()
    queue = deque()
    
    start = (sx, sy)
    visited.add(start)
    queue.append(start)
    
    while queue:
        cur = queue.popleft()
        for nxt in calculate(cur[0], cur[1]):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    print(len(visited))

main()