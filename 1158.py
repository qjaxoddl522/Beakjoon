N, K = map(int, input().split())
yp = []
arr = [i for i in range(1, N+1)]
num = 0

for _ in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)
    yp.append(str(arr[num]))
    arr.pop(num)

print("<",', '.join(yp),">", sep="")
