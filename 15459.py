import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
taste = [] # [맛, 매운맛]
for _ in range(N):
    taste.append(list(map(int, input().split())))

spicyMin = int(1e10) # 조건을 만족하는 최소 매운맛(정답)
tasteSum = 0
dq = deque() # 현재 구간의 매운맛 최댓값 유지

start = 0 # 시작점
for end in range(N):
    tasteSum += taste[end][0]
    
    # 현재 구간에서 가장 매운맛이 맨 앞에 오도록 유지
    while dq and dq[-1][1] <= taste[end][1]:
        dq.pop()
    dq.append((end, taste[end][1]))
    
    while tasteSum >= M:
        # 현재 구간의 매운맛 최댓값
        spicyMin = min(spicyMin, dq[0][1])
        
        tasteSum -= taste[start][0]
        
        # 구간의 시작점을 옮기면서 데크도 갱신
        if dq and dq[0][0] == start:
            dq.popleft()
        start += 1

print(spicyMin)
