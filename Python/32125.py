import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    N, K = map(int, input().split())
    cnt = 0
    
    taskType = list(map(int, input().split()))
    efficiency = list(map(int, input().split()))
    for i, num in enumerate(efficiency):
        if taskType[i] != 1:
            efficiency[i] *= -1
    
    # 능률 구간합
    efficiencySumArr = [0]
    for i in range(N):
        efficiencySumArr.append(efficiencySumArr[i] + efficiency[i])
    
    # 각 구간합의 갯수와 인덱스
    taskTypeDict = {0: [-1]}
    taskTypeSum = 0
    for i, num in enumerate(taskType):
        if num == 1:
            taskTypeSum += 1
        else:
            taskTypeSum -= 1
        
        # 현재까지 구간합이 딕셔너리에 존재하면 능률 확인 후 cnt 추가
        if taskTypeSum in taskTypeDict:
             for start in taskTypeDict[taskTypeSum]:
                 # (start+1, i)
                 if abs(efficiencySumArr[i+1] - efficiencySumArr[start+1]) <= K:
                     cnt += 1

        if taskTypeSum in taskTypeDict:
            taskTypeDict[taskTypeSum].append(i)
        else:
            taskTypeDict[taskTypeSum] = [i]
    
    return cnt

for _ in range(int(input())):
    print(solve())
