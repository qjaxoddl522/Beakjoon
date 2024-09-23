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

for i in range(1, N):
    if line[i] > LIS[-1]:
        LIS.append(line[i])
    else:
        LIS[binarySearch(line[i])] = line[i]

# 최소로 잘라야 하는 전선 수
print(N - len(LIS))
