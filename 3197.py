import sys
input = sys.stdin.readline
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

#물가 번호의 루트 찾기
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

R, C = map(int, input().split())
#방문한 물가 번호
visited = [[0] * R for i in range(C)]

q = deque()
for i in range(1, 1)
