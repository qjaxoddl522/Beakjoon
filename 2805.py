n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    summ = 0 
    for i in tree:
        summ += max(0, i - mid)
    
    if summ >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
