import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ls = sorted(list(map(int, input().split())))

left = 0
right = len(ls) - 1
minv = abs(ls[left] + ls[right])
ans = [ls[left], ls[right]]

while left < right:
    sumv = ls[left] + ls[right]
    if minv > abs(sumv):
        minv = abs(sumv)
        ans = [ls[left], ls[right]]
    
    if sumv < 0:
        left += 1
    elif sumv > 0:
        right -= 1
    else:
        break
print(*ans)
