import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N = int(input())
    graph = [[] for _ in range(N+1)]
    inner = [0 for _ in range(N+1)]
    time = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        inp = list(map(int, input().split()))
        time[i] = inp[0]
        for j in inp[1:-1]:
            graph[j].append(i)
            inner[i] += 1
    
    result = [0 for _ in range(N+1)]
    dq = deque()
    for i in range(1, N+1):
        if inner[i] == 0:
            result[i] = time[i]
            dq.append(i)
    
    for _ in range(N):
        node = dq.popleft()
        for next in graph[node]:
            inner[next] -= 1
            result[next] = max(result[next], result[node] + time[next])
            if inner[next] == 0:
                dq.append(next)
    print('\n'.join(map(str, result[1:])))

main()