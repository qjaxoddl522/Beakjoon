import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
k = int(input())

left = 1
right = N**2
ans = 0
while left <= right:
    mid = (left + right) // 2
    
    num = 0 # mid 이하의 수 갯수
    for i in range(1, N+1):
        num += min(mid//i, N)

    # 갯수가 너무 많음
    if num >= k:
        ans = mid
        right = mid - 1
    # 갯수가 너무 적음
    else:
        left = mid + 1
        
print(ans)
