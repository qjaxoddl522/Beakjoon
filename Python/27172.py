import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
card = []
score = dict()

M = 0 # 입력 숫자 중 최댓값
for idx, num in enumerate([*map(int, input().split())]):
    M = max(M, num)
    card.append((idx, num))
    score[num] = 0

card.sort(key=lambda x:x[1])

for i in range(N):
    idx, num = card[i]

    for op in range(num*2, M+1, num):
        # op는 num 배수이므로 존재하면 무조건 op 패배
        if op in score:
            score[num] += 1
            score[op] -= 1

print(*score.values())
