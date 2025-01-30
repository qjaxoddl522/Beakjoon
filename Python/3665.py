import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    n = int(input())
    prev = list(map(int, input().split()))
    
    graph = [set() for _ in range(n+1)]
    inner = [0 for _ in range(n+1)]
    # 작년 순위관계 생성
    for i in range(n):
        for j in range(i+1, n):
            graph[prev[i]].add(prev[j])
            inner[prev[j]] += 1
    
    # 바뀐 순위관계 반영
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].discard(a)
            inner[a] -= 1
            graph[a].add(b)
            inner[b] += 1
        elif b in graph[a]:
            graph[a].discard(b)
            inner[b] -= 1
            graph[b].add(a)
            inner[a] += 1

    dq = deque()
    for i in range(1, n+1):
        if inner[i] == 0:
            dq.append(i)
    
    result = []
    for _ in range(n):
        if not dq:
            print("IMPOSSIBLE")
            return
        if len(dq) > 1:
            print("?")
            return
        node = dq.popleft()
        result.append(node)
        for next in graph[node]:
            inner[next] -= 1
            if inner[next] == 0:
                dq.append(next)
    print(*result)

for _ in range(int(input())):
    main()