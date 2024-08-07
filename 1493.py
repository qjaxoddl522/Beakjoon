import sys
input = lambda: sys.stdin.readline().rstrip()

length, width, height = map(int, input().split())
N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]

vol = length * width * height
result = 0
filled = 0 # 이미 채운 부피
cube.sort(reverse=True)

size = 2 ** cube[0][0]
for cid, cnt in cube:
    filled *= 8
    # 채우기 위해 남은 큐브 수
    remainCnt = (length // size) * (width // size)\
                * (height // size) - filled
    filledCnt = min(cnt, remainCnt) # 채울 큐브 수
    result += filledCnt
    filled += filledCnt

    size //= 2

print(result if filled == vol else -1)
