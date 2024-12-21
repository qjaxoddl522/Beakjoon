import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    K, M, P = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    inner = [0] * (M+1)
    for _ in range(P):
        x, y = map(int, input().split())
        graph[x].append(y)
        inner[y] += 1
    
    # [strahler, 들어온 최대 strahler, 그 strahler의 수]
    strahler = [[0, 0, 0] for _ in range(M+1)]
    dq = deque()
    for i in range(1, M+1):
        if inner[i] == 0:
            strahler[i][0] = 1
            dq.append(i)
    
    for _ in range(M):
        node = dq.popleft()
        for next in graph[node]:
            inner[next] -= 1
            if strahler[next][1] < strahler[node][0]:
                strahler[next][1] = strahler[node][0]
                strahler[next][2] = 0
            if strahler[next][1] == strahler[node][0]:
                strahler[next][2] += 1
                if strahler[next][2] >= 2:
                    strahler[next][0] = strahler[node][0] + 1
                else:
                    strahler[next][0] = strahler[node][0]
            if inner[next] == 0:
                dq.append(next)
    print(K, strahler[node][0])

for _ in range(int(input())):
    main()