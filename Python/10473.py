import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
    start = tuple(map(float, input().split()))
    end = tuple(map(float, input().split()))

    n = int(input())
    graph = [[] for _ in range(n+2)]
    cannon = [None] + [tuple(map(float, input().split())) for _ in range(n)]
    graph[0].append((n+1, get_dist(start, end)/5))
    for i in range(1, n+1):
        # 시작점에서 대포
        graph[0].append((i, get_dist(start, cannon[i])/5))
        for j in range(1, i):
            # 캐논타기 또는 걸어가기
            dist = get_dist(cannon[i], cannon[j])
            time = min(2+abs(dist-50)/5, dist/5)
            graph[i].append((j, time))
            graph[j].append((i, time))
        # 대포에서 도착점
        dist = get_dist(cannon[i], end)
        time = min(2+abs(dist-50)/5, dist/5)
        graph[i].append((n+1, time))
    
    # 다익스트라 수행
    dis = [0] + [float('inf')] * (n+1)
    visited = [False] * (n+2)
    hq = [(0, 0)]
    while hq:
        nowd, now = heappop(hq)
        visited[now] = True
        for next, nextd in graph[now]:
            if not visited[next] and dis[next] > nowd + nextd:
                dis[next] = nowd + nextd
                heappush(hq, (dis[next], next))
    print(dis[n+1])

def get_dist(c1, c2):
    return (abs(c1[0]-c2[0])**2 + abs(c1[1]-c2[1])**2)**(1/2)

main()