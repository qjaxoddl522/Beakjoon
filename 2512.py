N = int(input())
request = list(map(int, input().split()))
budget = int(input())

low, high = 0, max(request)+1 #low 이상 high 미만

while(low+1 < high):
    mid = (low+high)//2

    budget_sum = 0
    for i in request:
        budget_sum += min(i, mid)

    if budget_sum <= budget: #예산 충족
        low = mid
    else: #예산 초과
        high = mid

print(low)
