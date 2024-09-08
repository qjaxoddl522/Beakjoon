import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

ans = float('inf')
sIdx = 0
for e in array:
    while sIdx < N and e - array[sIdx] >= M:
        ans = min(ans, e - array[sIdx])
        sIdx += 1
print(ans)