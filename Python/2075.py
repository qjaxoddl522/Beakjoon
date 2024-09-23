import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())
q = list(map(int, input().rstrip().split()))

#메모리 절약을 위해 최소힙에 N개씩 push와 pop을 반복
for _ in range(N-1):
    put = list(map(int, input().rstrip().split()))
    for i in put:
        hq.heappush(q, i)
        hq.heappop(q)
#크기가 N이므로 N번째 큰 수는 최소힙의 top
print(hq.heappop(q))
