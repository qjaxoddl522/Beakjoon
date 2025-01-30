import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main() -> None:
    n = int(input())
    sign = list(input().split())
    
    graph = [[] for _ in range(n+1)]
    inner_max = [0 for _ in range(n+1)]
    inner_min = [0 for _ in range(n+1)]
    for i in range(n):
        if sign[i] == '<':
            graph[i+1].append(i)
            inner_max[i] += 1
            inner_min[i] += 1
        else:
            graph[i].append(i+1)
            inner_max[i+1] += 1
            inner_min[i+1] += 1
    
    hq_max = []
    hq_min = []
    for i in range(n+1):
        if inner_max[i] == 0:
            heappush(hq_max, i)
            heappush(hq_min, -i)
    
    temp = 0
    result_max = [-1] * (n+1)
    for _ in range(n+1):
        node = heappop(hq_max)
        result_max[node] = 9-temp
        temp += 1
        for next in graph[node]:
            inner_max[next] -= 1
            if inner_max[next] == 0:
                heappush(hq_max, next)
    
    temp = 0
    result_min = [-1] * (n+1)
    for _ in range(n+1):
        node = -heappop(hq_min)
        result_min[node] = n-temp
        temp += 1
        for next in graph[node]:
            inner_min[next] -= 1
            if inner_min[next] == 0:
                heappush(hq_min, -next)
    
    print(''.join(map(str, result_max)))
    print(''.join(map(str, result_min)))

main()