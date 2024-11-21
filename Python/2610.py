import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

N = int(input())
M = int(input())
dist = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드 워셜
for m in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])

# 컴포넌트 수 계산 및 대표 선정
result = dict()
for i in range(1, N+1):
    comp = []
    maxDist = 0
    for j in range(1, N+1):
        if dist[i][j] != INF:
            comp.append(j)
            maxDist = max(maxDist, dist[i][j])
    comp = tuple(comp)
    if comp not in result or result[comp][0] > maxDist:
        result[comp] = (maxDist, i)

print(len(result))
srt = []
for _, delegate in result.items():
    srt.append(delegate[1])
for i in sorted(srt):
    print(i)