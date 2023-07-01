n, m = map(int, input().split())
file = list(map(int, input().split()))

start, end = sum(file)//m-1, sum(file)

while start+1 < end:
    mid = (start+end)//2
    possible = True
    
    summ = 0
    count = 1
    i = 0
    while i < n:
        if summ+file[i] <= mid:
            summ += file[i]
        elif count < m:
            summ = 0
            count += 1
            i -= 1
        else:
            possible = False
            break
        i += 1

    if not possible:
        start = mid
    else:
        end = mid
print(end)
