import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
card = list(map(int, input().split()))
score = [0] * N

for i in range(N):
    for j in range(i):
        if card[i] % card[j] == 0:
            score[i] -= 1
            score[j] += 1
        elif card[j] % card[i] == 0:
            score[i] += 1
            score[j] -= 1

print(*score)
