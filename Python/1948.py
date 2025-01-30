import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    n = int(input())
    m = int(input())
    time = [0] * (n+1)
    road = [[] for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    inner = [0] * (n+1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        inner[b] += 1
    
    s, e = map(int, input().split())
    dq = deque([s])
    for _ in range(n):
        node = dq.popleft()
        for next, nexttime in graph[node]:
            inner[next] -= 1
            if time[next] < time[node] + nexttime:
                time[next] = time[node] + nexttime
                road[next] = [node]
            if time[next] == time[node] + nexttime:
                road[next].append(node)
            if inner[next] == 0:
                dq.append(next)
    
    dq = deque([e])
    path = set()
    while dq:
        node = dq.popleft()
        for prev in road[node]:
            if (prev, node) not in path:
                path.add((prev, node))
                dq.append(prev)
    print(time[e])
    print(len(path))

main()