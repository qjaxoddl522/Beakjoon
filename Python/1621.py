import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    K, C = map(int, input().split())
    banana = list(map(int, input().split()))

    # i개에서 드는 시간의 최소
    dp = [0 for _ in range(N)]
    # None => K개를 들고가지 않음
    path = [None for i in range(N)]
    prefix = 0
    for i in range(K-1):
        prefix += banana[i]
        dp[i] = prefix
    for i in range(K-1, N):
        if dp[i-1] + banana[i] > dp[i-K] + C:
            dp[i] = dp[i-K] + C
            path[i] = i-K
        else:
            dp[i] = dp[i-1] + banana[i]
    
    # 경로 추적
    p = []
    i = N-1
    while i >= 0:
        if path[i] != None:
            # 묶음 시작번호와 넘버링 => +2
            p.append(path[i]+2)
            i = path[i]
        else:
            i -= 1

    print(dp[N-1])
    print(len(p))
    for i in range(len(p)-1, -1, -1):
        print(p[i])

main()