import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for m in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if graph[s][e] == 0 and graph[s][m] == 1 and graph[m][e] == 1:
                graph[s][e] = 1

# 둘 중에 하나라도 연결되어 있으면 키를 비교할 수 있는 것
answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and graph[i][j] == 0 and graph[j][i] == 0:
            break
    else:
        answer += 1
print(answer)