import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_TIME = 999999

# 문제 수, 참가자 수, 기록 수
N, M, P = map(int, input().split())
record = {}
score = {}
nameList = list(input().split())
for name in nameList:
    record[name] = [[] for _ in range(N+1)]
    score[name] = 0

# 기록 입력
for _ in range(P):
    problem, time, name, isSolve = input().split()
    problem = int(problem)
    record[name][problem].append((time, isSolve))

# 점수 계산
for problem in range(1, N+1):
    # [해결 시간, 이름]
    rank = []
    for name, info in record.items():
        isSolved = False
        firstWrongTime = "00:00"
        for time, isSolve in info[problem]:
            if isSolve == "solve":
                if firstWrongTime != "00:00":
                    # 해결 시간 계산
                    hour, minute = map(int, time.split(':'))
                    minute = (hour * 60) + minute
                    firstHour, firstMinute = map(int, firstWrongTime.split(':'))
                    minute -= (firstHour * 60) + firstMinute
                    rank.append([minute, name])
                isSolved = True
                break
            elif firstWrongTime == "00:00":
                firstWrongTime = time
        # 시도했으나 해결하지 못함
        if not isSolved and firstWrongTime != "00:00":
            rank.append([MAX_TIME, name])
    
    rank.sort(key=lambda x: (x[0], x[1]))
    for name in nameList:
        isExists = False
        for _, n in rank:
            if name == n:
                isExists = True
                break
        if not isExists:
            rank.append([-1, name])
    
    for idx, row in enumerate(rank):
        if row[0] == -1:
            score[row[1]] += M+1
        elif row[0] == MAX_TIME:
            score[row[1]] += M
        else:
            score[row[1]] += idx+1

# 정렬 후 출력
finalRank = sorted(score.items(), key=lambda x: (x[1], x[0]))
for name, _ in finalRank:
    print(name)
