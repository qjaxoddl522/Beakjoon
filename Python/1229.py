import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    hexa = []
    next = 1
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    i = 1
    for n in range(1, N+1):
        if n >= next:
            hexa.append(next)
            i += 1
            # 이전 + 육각형의 변 - 겹치는 부분
            next = hexa[-1] + i*6-6 - ((i-1)*2-1)
        for j in range(len(hexa)):
            dp[n] = min(dp[n], dp[n-hexa[j]] + 1)
    print(dp[N])

main()