import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    N, M, K = map(int, input().split())
    rsp = [[] for _ in range(N)]
    for i in range(N):
        rsp[i] = input()

    for r in range(1, M+1):
        rspDict = dict()
        for i in range(N):
            st = rsp[i][:r]
            if st in rspDict:
                rspDict[st] += 1
            else:
                rspDict[st] = 1

        rspMinKey = min(rspDict, key=rspDict.get)
        if rspDict[rspMinKey] <= K:
            return (r, rspMinKey)
    return -1

result = solve()
if result == -1:
    print(result)
else:
    print(result[0])
    # 정답 출력을 위해 지는 가위바위보로 변환
    table = str.maketrans('RSP', 'SPR')
    print(result[1].translate(table))
