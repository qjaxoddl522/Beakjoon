import sys
input = lambda: sys.stdin.readline().rstrip()

def binarySearch(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start
while True:
    try:
        N = int(input())
        A = list(map(int, input().split()))
        LIS = [A[0]]

        for i in range(N):
            # LIS의 마지막 값과 비교하여 더 큰 경우에만 삽입
            if A[i] > LIS[-1]:
                LIS.append(A[i])
            #아닐 경우 이분 탐색된 위치를 변경시킴
            else:
                LIS[binarySearch(A[i])] = A[i]

        print(len(LIS))
    except:
        break
