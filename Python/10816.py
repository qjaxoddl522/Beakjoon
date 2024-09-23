import sys
input = sys.stdin.readline

n = int(input())
cardN = list(map(int, input().split()))
m = int(input())
cardM = list(map(int, input().split()))

card = {}
for i in cardN:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

for i in cardM:
    if i in card:
        print(card[i], end=' ')
    else:
        print(0, end=' ')
