import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main() -> None:
    N = int(input())
    M = int(input())
    # 부품 i를 조립하는 데 필요한 기본 부품 j의 개수
    needs = [[0] * (N+1) for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    inner = [0 for _ in range(N+1)]
    for _ in range(M):
        X, Y, K = map(int, input().split())
        graph[Y].append((X, K))
        inner[X] += 1

    dq = deque()
    for i in range(1, N+1):
        if inner[i] == 0:
            needs[i][i] = 1
            dq.append(i)
    
    for _ in range(N):
        node = dq.popleft()
        for next, need in graph[node]:
            inner[next] -= 1
            for i in range(1, N+1):
                needs[next][i] += needs[node][i]*need
            if inner[next] == 0:
                dq.append(next)
    
    for i in range(1, N+1):
        if needs[N][i] > 0:
            print(f"{i} {needs[N][i]}")

main()