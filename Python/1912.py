n = int(input())
ls = list(map(int, input().split()))

for i in range(1, n):
    ls[i] = max(ls[i], ls[i-1]+ls[i]) #앞쪽의 합과 비교하여 큰 수만을 남김
print(max(ls))
