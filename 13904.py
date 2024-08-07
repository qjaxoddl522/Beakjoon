import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
task = []
for _ in range(N):
    task.append(list(map(int, input().split())))
task.sort(key=lambda x: -x[1])

# 점수 내림차순으로 최대한 늦게 과제 수행
plan = [0] * max([x[0] for x in task])
for deadline, score in task:
    # 아직 계획에 없으면 추가
    for date in range(deadline, 0, -1):
        if plan[date-1] == 0:
            plan[date-1] = score
            break

print(sum(plan))
