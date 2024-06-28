import sys
input = lambda: sys.stdin.readline().rstrip()
import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

    #둘의 좌표가 같음
    if dist == 0:
        #거리도 같으면 무한대
        if r1 == r2:
            print(-1)
        #거리가 다르면 없음
        else:
            print(0)
    
    #둘의 좌표가 다름
    else:
        rSum = r1 + r2
        rDiff = abs(r1 - r2)
        #두 원이 안쪽 또는 바깥쪽에서 만남
        if rDiff < dist < rSum:
            print(2)
        #외접 또는 내접
        elif dist == rSum or dist == rDiff:
            print(1)
        else: #만나지 않음
            print(0)
