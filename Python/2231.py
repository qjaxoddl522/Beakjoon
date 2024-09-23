n = int(input())
result = 0
for m in range(n):
    summ = m
    for i in str(m):
        summ += int(i)
    if summ == n:
        result = m
        break
print(result)
