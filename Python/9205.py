import sys
input = lambda: sys.stdin.readline().rstrip()

# 플로이드-워셜 풀이
for _ in range(int(input())):
    n = int(input())
    # 0:home    n+1:rock
    dist = [[0] * (n+2) for _ in range(n+2)]
    coor = []
    for i in range(n+2):
        r, c = map(int, input().split())
        for j in range(i):
            if abs(r-coor[j][0]) + abs(c-coor[j][1]) <= 1000:
                dist[i][j] = 1
                dist[j][i] = 1
        coor.append((r, c))
    for m in range(n+2):
        for s in range(n+2):
            for e in range(n+2):
                if dist[s][e] == 0 and dist[s][m] == 1 and dist[m][e] == 1:
                    dist[s][e] = 1
    print("happy" if dist[0][n+1] == 1 else "sad")