import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    def dijkstra(start):
        visited = [False] * (n+1)
        result = 0
        # (이동한 거리, 현재 지점)
        hq = [(0, start)]
        while hq:
            moved, node = heappop(hq)
            if visited[node] or moved > m:
                continue
            visited[node] = True

            result += item[node]
            for next, dist in graph[node]:
                if not visited[next]:
                    heappush(hq, (moved + dist, next))
        return result
        
    n, m, r = map(int, input().split())
    item = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))

    answer = 0
    for st in range(1, n+1):
        answer = max(answer, dijkstra(st))
    print(answer)

main()