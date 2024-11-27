import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

N, R = map(int, input().split())
names = list(input().split())
numbers = {}
for i in range(N):
    numbers[names[i]] = i

M = int(input())
path = list(input().split())

# 교통수단 저장
K = int(input())
line = []
for _ in range(K):
    line.append(input().split())

# 내일로 티켓을 샀을 경우와 사지 않았을 경우 비용 각각 계산
dist_basic = [[INF] * N for _ in range(N)]
dist_tomorrow = [[INF] * N for _ in range(N)]
for t, s, e, c in line:
    c = float(c)
    dist_basic[numbers[s]][numbers[e]] = min(dist_basic[numbers[s]][numbers[e]], c)
    dist_basic[numbers[e]][numbers[s]] = min(dist_basic[numbers[e]][numbers[s]], c)

    if t == "Mugunghwa" or t == "ITX-Saemaeul" or t == "ITX-Cheongchun":
        c = 0
    elif t == "S-Train" or t == "V-Train":
        c = c/2
    dist_tomorrow[numbers[s]][numbers[e]] = min(dist_tomorrow[numbers[s]][numbers[e]], c)
    dist_tomorrow[numbers[e]][numbers[s]] = min(dist_tomorrow[numbers[e]][numbers[s]], c)

result_basic, result_tomorrow = 0, R
for m in range(N):
    for s in range(N):
        for e in range(N):
            dist_basic[s][e] = min(dist_basic[s][e], dist_basic[s][m] + dist_basic[m][e])
            dist_tomorrow[s][e] = min(dist_tomorrow[s][e], dist_tomorrow[s][m] + dist_tomorrow[m][e])
for i in range(M-1):
    result_basic += dist_basic[numbers[path[i]]][numbers[path[i+1]]]
    result_tomorrow += dist_tomorrow[numbers[path[i]]][numbers[path[i+1]]]

print("Yes" if result_basic > result_tomorrow else "No")