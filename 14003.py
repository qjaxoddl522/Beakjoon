import sys
input = lambda: sys.stdin.readline().rstrip()

# 이분 탐색
def binarySearch(e):
    start = 0
    end = len(LIS)
    
    while start < end:
        mid = (start + end) // 2
        
        if LIS[mid] < e:
            start = mid + 1
        else:
            end = mid
            
    return start

N = int(input())
line = list(map(int, input().split()))
LIS = [line[0]]
LIS_ans = [(line[0], 0)]

for i in range(1, N):
    if line[i] > LIS[-1]:
        LIS_ans.append((line[i], len(LIS)))
        LIS.append(line[i])
    else:
        idx = binarySearch(line[i])
        LIS_ans.append((line[i], idx))
        LIS[idx] = line[i]

print(len(LIS))

# 인덱스 기반 역추적
lastIdx = len(LIS) - 1
ans = []
for i in range(len(LIS_ans)-1, -1, -1):
    # i번째 값의 인덱스와 일치하면 LIS에 들어감
    if LIS_ans[i][1] == lastIdx:
        ans.append(LIS_ans[i][0])
        lastIdx -= 1

print(*ans[::-1])
