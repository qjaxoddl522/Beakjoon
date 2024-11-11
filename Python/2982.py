import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

"""
다익스트라를 할 때 현재 진입 불가능한 간선을 이용해야할 경우
고둘라가 지나갈 때까지 기다렸다 이동
"""
def dijkstra(start):
    time = [float('inf')] * (N+1)
    time[start] = K
    hq = [(K, start)]
    while hq:
        curtime, curnode = heapq.heappop(hq)
        if curnode == B:
            return curtime - K
        for nextnode, t in graph[curnode].items():
            if (curnode, nextnode) in banned:
                banstart, banend = banned[(curnode, nextnode)]
                # 금지구간과 시간에 포함되면 기다렸다가 이동
                if banstart <= curtime < banend and time[nextnode] > banend + t:
                    time[nextnode] = banend + t
                    heapq.heappush(hq, (time[nextnode], nextnode))
                # 구간만 포함이면 평소처럼 이동
                elif not (banstart <= curtime < banend) and time[nextnode] > curtime + t:
                    time[nextnode] = curtime + t
                    heapq.heappush(hq, (time[nextnode], nextnode))
            # 구간에 포함되지 않음
            elif time[nextnode] > curtime + t:
                time[nextnode] = curtime + t
                heapq.heappush(hq, (time[nextnode], nextnode))

# 교차로(노드) 수, 도로 수
N, M = map(int, input().split())
# 출발, 도착, 상근이 출발 시간, 고둘라 방문 교차로 개수
A, B, K, G = map(int, input().split())
godula = list(map(int, input().split()))

graph = [dict() for _ in range(N+1)]
for _ in range(M):
    u, v, l = map(int, input().split())
    graph[u][v] = l
    graph[v][u] = l

# (사용 불가능한 구간) : (사용 불가능한 시간)
banned, curtime = {}, 0
for i in range(G-1):
    s, e = godula[i], godula[i+1]
    t = graph[s][e]
    banned[(s, e)] = (curtime, curtime + t)
    banned[(e, s)] = (curtime, curtime + t)
    curtime += t

result = dijkstra(A)
print(result)