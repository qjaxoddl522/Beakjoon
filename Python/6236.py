N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

bot, top = min(money), sum(money)
result = 0

while(bot <= top):
    mid = (bot + top) // 2
    num, K = 1, 0 #횟수, 하루 누적 인출 금액

    for i in money:
        if K + i <= mid: #기준 금액 미초과
            K += i
        else: #기준 금액 초과
            num += 1
            K = i

    if M < num or mid < max(money): #인출 횟수 초과 또는 인출 금액 하루 초과
        bot = mid + 1
    else:
        top = mid - 1
        result = mid

print(result)
