import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

N = int(input())
dist = []
for _ in range(N):
    dist.append(list(map(int, input().split())))

def restore():
    graph = [dist[i][:] for i in range(N)]
    for m in range(N):
        for s in range(N):
            if m != s:
                for e in range(N):
                    if s != e and m != e:
                        if dist[s][e] == dist[s][m] + dist[m][e]:
                            graph[s][e] = 0
                        elif dist[s][e] > dist[s][m] + dist[m][e]:
                            return -1
    result = 0
    for i in range(N):
        result += sum(graph[i])
    return result // 2
print(restore())