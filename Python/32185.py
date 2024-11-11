import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
player = tuple(map(int, input().split()))
playerSum = sum(player)
others = []
for i in range(N):
    otherSum = sum(list(map(int, input().split())))
    if otherSum <= playerSum:
        others.append((otherSum, i+1))
others.sort(key=lambda x: -x[0])

answer = [0]
for i in range(min(len(others), M-1)):
    answer.append(others[i][1])
print(*answer)