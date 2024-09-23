import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

bot, top = 1, max(lan)
ans = 0

while(bot <= top):
    mid = (bot + top) // 2
    n = 0
    for i in lan:
        n += i // mid

    if n >= N: #가능
        bot = mid + 1
        ans = mid
    else: #불가능
        top = mid - 1

print(ans)
